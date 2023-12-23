text = input('Введите любую строку')
konectext = ''
al = 'йЙяЯыЫуУАаеЕиИоОюЮэЭaAeEyYuUiIoO'
st = text.split()
for i in range(0,len(st)):
    slovo = list(st[i])
    if slovo[0] not in al:
        konectext += ' ' + st[i]
print(konectext.split(','),'KONEC')

