# sbwm-backend

exec

```
./sbwm-run.sh
```

-----

#endPoint
GET
```
/
```

output:

```
"hello world"
```

-----

POST

```
/load
``` 

input: 

```
{
img_file: image URL
}
```

ex:

```
{
img_file: "https://res.cloudinary.com/dagcggcea/image/upload/v1616280128/image_test_wlltdw.png"
}
```

output:

```
status': '200', 'data': {'red': {'text': [], 'square': []}, 'blue': {'text': [], 'square': [}, 'green': {'text': [], 'square': []}, 'Black': {'text': [], 'square': []}}} 
```

ex:

```

{'status': '200', 'data': {'red': {'text': [], 'square': []}, 'blue': {'text': ['HAckPay'], 'square': ['ホワイトボード', '使う']}, 'green': {'text': [], 'square': []}, 'Black': {'text': ['家決め大変···', 'OCR仗?!', '·ネットワーク良い!!', 'ホワイトボード', '使う'], 'square': []}}}
```
