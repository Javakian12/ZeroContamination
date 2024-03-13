# CSCI198-ZeroWaste

ZeroContamination. Yolov7 credit to WongKinYiu, https://github.com/WongKinYiu/yolov7. Segmenter tool credit to https://github.com/GeorgeSeif/Semantic-Segmentation-Suite

Setup:

To setup this tool you need to install Yolov7 and Semantic-Segmentation-Suite-master. Here is the link to Semantic-Segmentation-Suite-master: https://github.com/GeorgeSeif/Semantic-Segmentation-Suite and here is the link to YoloV7: https://github.com/WongKinYiu/yolov7. The weights can be downloaded via the website: https://www.apanagopoulos.com. 

Please note, if you are setting this tool up on a server you need to install the architectures (YoloV7 and Semantic-Segmentation-Suite-master) as well as python and anaconda on the server for this to work correctly. Same goes if you are setting this up on your own local machine, however you will be using localhost instead of a reverse proxy on a server.

Step 1:

Create a file called YoloV7 in the same directory as back-end.

Download YoloV7 to this directory, setup YoloV7 following their guide, then download the weights for YoloV7. This should be in one large zip file that contains FRNN-A and DeepLabV3's weights also. 

Create a folder named "zerowaste-lr0_0001-ep100" (you can name it something else if you like) and place this in the YoloV7 yolov7/runs/train/ directory.

Create a subfolder in this directory called weights, then place the weights in this folder (unzip/decompress them first).

Step 2:

Download the Semantic-Segmentation-Suite-master github repository, and place it in the same directory as back-end.

Create a folder in the Semantic-Segmentation-Suite-master directory named image_test.

Download and unzip/decompress the FRNNA weights and place them in the image_test folder, as well as the class_dict.csv file in this same folder (this file can be downloaded off of the github repository under the class_dict folder).

Place the same class_dict.csv file in a folder called "dataset" in the Semantic-Segmentation-Suite-master directory (create the folder if you don't have it).

Step 3:

Now that you have both architectures downloaded, you need to set them up. Unfortunately both use different versions of python and different ML architectures, so we will have to use Conda. If you want to try, you can download the dependencies for the architectures without using conda, but I don't recommend it as you will have conflicting versions of python downloaded.

Download anaconda, setup a conda environment (name it test), and set the python version to 3.6.3 (this is very important!!!).

Download the dependencies for Semantic-Segmentation-Suite-master (you can find them in the Semantic-Segmentation-Suite-master github repository) in the conda environment (they require python 3.6.3, which is why you must set it at this verision).

Now that you have setup this environment, setup YoloV7 by installing the correct dependencies. You don't need to use conda for this, just use your regular console/python shell.

Step 4:

At this point you should be able to run both architectures (YoloV7 and Semantic-Segmentation-Suite-master). We need to edit the back-end files so it is compatible on your machine.

Navagate to the back-end directory and open app.js. The other files are used for specific functions when training the model (data-preprocessing) so these can be ignored for now.

In app.js, navigate to the line: 

      "exec(`cd .. && cd Semantic-Segmentation-Suite-master && conda run -n test python predict.py --image ../back-end/${i}.jpg --checkpoint_path image_test/model.ckpt --crop_height 640 --crop_width 640 --model FRRN-A --dataset dataset`, (err) => { "
      
Ensure that the "conda run -n test" matches your conda environment name (if you did not name it test, replace test with the name).

Navigate to the line:

      "exec(`cd .. && cd yolov7 && python detect.py --weights runs/train/zerowaste-lr0_0001-ep100/weights/best.pt --conf 0.25 --save-txt --img-size 640 --source inference/images/${name}`, (err, output) => { "
      
Make sure that "zerowaste-lr0_0001-ep100" matches the name of the folder you put the YoloV7 weights in. 

We need to also install the dependencies for react. Navigate to front-end/zeroWaste, and run yarn install. If yarn is not installed, install it using npm then try the command again. For each dependency that yarn says it can't find, run the command: yarn add "dependency name" (replace dependency name with the name of the library you are installing). Do this until it has no more dependency issues.

✨ Now for the fun stuff ✨


Set the origin under the socketIo constructor to your correct hyperlink. You will have to do the same in the front-end directory, where you do "setAppSocket" in uploadImage.jsx under front-end/zeroWaste/src/elements. For good measure, if this isn't a local machine you might want to place this entire useEffect as well as the useEffect that console.log's the socketio status inside of the App.js fole in the zeroWaste folder (this will force the client to connect upon loading the tool via the webapp, versus connecting when they select upload image).

There may be one-offs, but you want to ensure that the front-end and back-end are communicating via socketio and the front end is recieving its session token. You also want to change the cors content policy to allow access-control-headers or your clients will be spammed with errors in their console.

Lastly, you will want to run through all the exec() commands in app.js and ensure they are pointing to the right directories/subfolders. This is the main point of failure/bugs in the back-end.

Load the server by opening a shell on your server/device and navigate to the back-end directory. Run the command: "node app.js"

Make sure you have the folder "runs" in your main directory (this is where the results are stored), and you should be able to run this app! To run, we will use Expo. In the console in the front-end/zeroWaste directory, run "yarn start" or "yarn expo start" then hit "w" for web. The app should load voluntarily.


Training

If you would like to re-train the model or add further information to it, you can do so by navigating to the contamination_data folder and downloading the .zip file, or by using this link: [Contamination Data](https://github.com/Javakian12/ZeroContamination/raw/main/contamination_data/zeroWaste_contamination_data.zip)

Download the class_dict.csv file as well if you plan on running a segmentation model: [class_dict]()

At this point, follow the training guidlines as described in the Yolo repository, replacing their data with this folder. Make sure to edit the 




Credit and License:
Copyright (c) 2023 Joshua Avakian.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Please feel free to cite me if you would like to continue this research.

The datasets involved is a derivative work of Zerowaste (http://ai.bu.edu/zerowaste/):

**Bashkirova, Dina, Mohamed Abdelfattah, Ziliang Zhu, James Akl, Fadi Alladkani, Ping Hu, Vitaly Ablavsky, Berk Calli, Sarah Adel Bargal, and Kate Saenko. "Zerowaste dataset: Towards deformable object segmentation in cluttered scenes." In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 21147-21157. 2022.**

YoloV7 Model:
**@misc{wang2022yolov7,
      title={YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors}, 
      author={Chien-Yao Wang and Alexey Bochkovskiy and Hong-Yuan Mark Liao},
      year={2022},
      eprint={2207.02696},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}**

Semantic_S
