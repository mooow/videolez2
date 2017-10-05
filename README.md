# Video-lessons url grabber

Example usage:
```
$ python3 videolez.py 'https:⁢//elearning.polito.it/gadgets/video/template_video.php?...' > links.txt
$ wget -c -i links.txt
```

You might also use `xargs -n 1 curl -O < links.txt` instead, but wget allows pausing/resuming downloads and also features an arguably nicer output

## Dependences
* lxml
* requests

You should be able to install them by running:
```
$ pip3 install -U --user lxml requests
```
Or see use the packages provided by your distribution (recommended.)
