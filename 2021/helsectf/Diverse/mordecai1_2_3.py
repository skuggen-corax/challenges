from itertools import product
from pwn import remote, log, context
from random import choice

RIKTIG_STED = "🏴"
FEIL_STED = "🏳️"

context.log_level = "info"


def generate_all_possibilities():
    tegn = ("🐰", "🐇", "🐣", "🐤", "🐥", "🥚")
    return [p for p in product(tegn, repeat=4)]


def scoring(gjett, test):
    assert len(gjett) == len(test)
    rette = 0
    nesten = 0
    sjekket = [False] * len(gjett)
    for i in range(len(gjett)):
        if gjett[i] == test[i]:
            rette += 1
            sjekket[i] = True

    for i in range(len(gjett)):
        if gjett[i] != test[i] and gjett[i] in test:
            for j in range(len(gjett)):
                if gjett[i] == test[j] and not sjekket[j]:
                    nesten += 1
                    sjekket[j] = True

    return (rette, nesten)


def main():
    c = remote('challenges.ctfd.io', 30035)
    c.recvuntil("send 4 tegn>")

    answers = []

    while len(answers) < 3:
        muligheter = generate_all_possibilities()
        guess = ("🐰", "🐰", "🐇", "🐇")
        svar = (0, 0)

        while svar[0] < 4:
            c.sendline("".join(guess))

            try:
                rep = c.recvline().decode()
            except EOFError:
                answers.append(rep)
                break

            svar = (rep.count(RIKTIG_STED), rep.count(FEIL_STED))
            log.debug("Sent %s, got %s", rep.strip(), svar)
            muligheter = [p for p in muligheter if svar == scoring(guess, p)]
            log.debug("muligheter: %s", len(muligheter))
            try:
                guess = choice(muligheter)
            except IndexError:
                log.info("Made a mess. Restarting..")
                main()

            try:
                next = c.recvuntil("send 4 tegn>")
            except EOFError:
                break

            if "👌" in next.decode():
                answers.append(next.decode())
                break

        log.progress("Finished "+str(len(answers))+"/3")

    print("".join((ans.split("}")[0]+"}\n" for ans in answers)))

    exit()

main()
