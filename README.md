# sbwm-backend

Lab:
https://github.com/s-taku3/imageLab
(画像をごちゃごちゃ弄って成功したpythonファイルをもらいました。)

------

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
img_file: image
}
```

output:

```
現状OCRの結果
```
