openssl pkey -outform der -pubin -in transparency_afff0345c6f99bf80eab5895458d8eab.pem| sha256sum

# gives 29ab37df0a4e4d252f0cf12ad854bede59038fdd9cd652cbc5c222edd26d77d2
# then goto https://censys.io/certificates?q=29ab37df0a4e4d252f0cf12ad854bede59038fdd9cd652cbc5c222edd26d77d2
