import asn1
import base64

encoded = "MIIEJaE3MDWgCQYHBAICAAUBDqEJBAdwZW5nd3luogQTAk5PoxAwDqAMMAqgCAQGU0FOVEVMpAUCAwj4k6KCA+ihggPkMIID4DAVoAMKAQCiDqAMBApjS0AET1JBSEAFMBCgAwoBAKIJoAcEBWtSQVYKMBCgAwoBAaIJoAcEBWxBTQoEMCKgAwoBAaIboBkEF2xFVgRAUQRCUUpKQVAESktBBEPnnF0bMBagAwoBAKIPoA0EC25FCARXQQRMQVYKMA6gAwoBAaIHoAUEAxsbBDAfoAMKAQGiGKAWBBRuQUMEV0FWBE1KQ0FKBFBNSkMKBDAboAMKAQCiFKASBBAODg4ODg4ODg4ODg4ODg4OMCigAwoBAaIhoB8EHW5BQwRXQVYERkVWQQQODg4ODg4ODg4ODg4ODg4OMDugAwoBAKI0oDIEMGtNCAROQUMER0tUXQtURVdQQVAEVEVXV0tWQEFQBElNUFAEUkFABEFKBEJBTUgKBDAeoAMKAQCiF6AVBBNmVkUEQEFQBEZIQQRXSEVAQEFQMBGgAwoBAaIKoAgEBk5BQ0FWFjANoAMKAQCiBqAEBAIbGzAdoAMKAQGiFqAUBBJgQVAEQlFKT0FQBE1PT0EKCgowG6ADCgEAohSgEgQQCgoKBFJBSlAESE1QUAQKCjAToAMKAQCiDKAKBAhAHUcXEkdHQjAPoAMKAQGiCKAGBARM54IbMA+gAwoBAKIIoAYEBBJFFxwwD6ADCgEAogigBgQEEBYcFTAPoAMKAQCiCKAGBARGEBxCMA+gAwoBAaIIoAYEBBsbGxswF6ADCgEAohCgDgQMQBUQQEYSHRBARUVBMBugAwoBAaIUoBIEEGxSRQRXQVYETkFDBFTngRkwI6ADCgEAohygGgQYYEFQBFdPRUgEUueCVkEEQUoEUVFNQAoEMCygAwoBAKIloCMEIWZNSkBBV1BWQU9PSkVUVEFKBElNSgRCUUpPQVYETU9PQTAroAMKAQGiJKAiBCBrQwRMUkUEQ0tAUARXT0VIBEBBUARDTuecVkEESUFDGzBPoAMKAQCiSKBGBERgUQRJ54EEUEUESUARBEVSBFFRTUADQUoEV0tJBEhLU0FWR0VXQQRMQVwES0MESEFDQ0EEUE1IBEBBUARSRUpITUNBCjAVoAMKAQGiDqAMBAp3T07nnEpKQVYFMB6gAwoBAaIXoBUEE2BBUARCUUpPQVYETU9PQQQKCgowNKADCgEAoi2gKwQpc0xLS1RXCgRxUU1AQUoEV09RSEhBBFdQRVZQQQRJQUAERx1HDAoKCg0wJaADCgEAoh6gHAQaCgoKBEtDBFdIUVBQQQRJQUAEDAoKCg0QRRcwFaADCgEBog6gDAQKc21qBQRwRU9PCjAYoAMKAQCiEaAPBA1xSkBBVgRLQwRNSkoK"
decoded = base64.b64decode(encoded)

decoder = asn1.Decoder()
decoder.start(decoded)

tag, value = decoder.read()

print (tag, value)