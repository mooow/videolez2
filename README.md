# Video-lessons url grabber

Example usage:
```
$ python3 videolez.py 'https:⁢//elearning.polito.it/gadgets/video/template_video.php?...' > links.txt
$ wget -c -i links.txt
```

You might also use `xargs -n 1 curl -O < links.txt` instead, but wget allows pausing/resuming downloads and also features an arguably nicer output

## Lower quality videos
Use option `-lq` to download lower quality videos (indicated as 'iPhone' on the website).

Example:
```
$ python3 videolez.py 'https:⁢//elearning.polito.it/gadgets/video/template_video.php?...' -lq > links_lq.txt
```

# Additional notes
If your link has format `https://elearning.polito.it/main/newscorm/lp_controller.php?...` this script
can't work. But if you follow this instructions you'll get a compatible URL.

1. Go to `Portale della didattica`
2. Go to the end `Videoteca lezioni on-line`
3. Click your course year (Primo anno, Magistrale, ...)
4. If you can find your course in the page that opens next, with a nice _*e*_ logo
on the side, click it
5. You should get a compatible link.

## Dependences
* lxml
* requests

You should be able to install them by running:
```
$ pip3 install -U --user lxml requests
```
Or see use the packages provided by your distribution (recommended.)
