# Face-Blur 
Ensure public privacy is upheld by applying automatic face blurring technology to live video steams in public or private areas such as train stations, shopping centers or privately owned businesses. Face blur is designed with privacy in mind. We can now easily blur faces to protect the privacy of all people recorded in video systems or in images. For the Face Blur feature to take effect, first, a face (or faces) needs to be detected in a video stream or in a still image(s). Once a face has been detected, similar to how your phone detects your face with a yellow bounding box when taking a selfie, we can then add a layer that blurs or pixelates the detected face(s). This happens in such a way that the person’s face can no longer be seen by the human eye. Our face detector is very strong and can detect faces from any angle and distance. The face blurring technology is robust therefore it can still accurately blur faces in large crowds. As long as the faces are not completely occluded then the software should apply the blur effect instantaneously.The first step in the system is capturing a frame in realtime from the camera of the computer. After that, the captured frames will be displayed on the computer screen. These frames are the basis for the next steps of the system. The captured frames dimensions are(640 480) pixels for width and height, respectively. Real-time systems always seek to reduce processing time for reliable results, video is the media that requires large resources to be processed. To minimize the number of resources used, avoid any additional unnecessary processes or operations.
Viola–Jones is an algorithm used for detection the faces that appear in front of the web camera. It accomplishes detection by performing the following four steps:
a. Haar like Feature to detects the areas of interest. 
b. Integral image to speeds up this process. 
c. Adaptive Boosting. 
d. Cascading classifiers
It is a process of masking the faces that appear on the screen, in order to hide theme when seeing them. In this research, Gaussian filter has been used to blurring the faces. The process of faces blurring is used in two different step, these are: 
i. Blurring the currently detected faces Each face currently detected by the Viola Jones algorithm will be directly blurred by using Gaussian filter. 
ii. Blurring selected areas to be faces Implement the blurring process by using Gaussian filter for each area that has been identified as a face
