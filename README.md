After deploying to `Jetson Nano`, due to the lack of memory on the Nano development board, an error occurs when calling multi-threaded playback of mp3 audio, as well as when calling the `pygame` library, it will not run. So in this branch of the code, the `pygame` library is removed, and the `GPIO` port on the development board is used to implement the mp3 audio playback function with the `BY8002` voice module.  

![ca8887bc235ab42e6f3b583cb2bd098.png](https://github.com/cccp421/CV-piano/blob/jetson/ca8887bc235ab42e6f3b583cb2bd098.png)
# run  
```
python3 run.py
```

## Jetson.GPIO User's Guide  
```
sudo pip install Jetson.GPIO
```
### Problems with GPIOs not working  
```
sudo chmod a+rw /dev/gpiochip0  
sudo chmod a+rw /dev/gpiochip1
```
