import streamlit as st
import pyrebase
from PIL import Image
import uuid
import cv2 

import webbrowser




# realtime image capture


# firebase config
config = {
  "apiKey": "AIzaSyAIx800R8uEyErKdDDC4nuF9j42s6MqmVA",
  "authDomain": "bfras-d8b76.firebaseapp.com",
  "databaseURL": "https://bfras-d8b76-default-rtdb.firebaseio.com",
  "storageBucket": "bfras-d8b76.appspot.com"
}

firebase = pyrebase.initialize_app(config)
firebase.database()
db = firebase.database()
storage = firebase.storage()
page_bg_img = '''
        <style>
        body {
        background-image: url("https://images.pexels.com/photos/1939485/pexels-photo-1939485.jpeg?cs=srgb&dl=pexels-henry-%26-co-1939485.jpg&fm=jpg"); 
            
}
        </style>
        '''

st.markdown(page_bg_img, unsafe_allow_html=True)

# main program
def main():
    st.title('BEAUTY FACE RECCOMEDATION AND ANALYSIS SYSTEM')
    url = 'http://localhost:8050'

   
    image_file = st.file_uploader("Upload Image",type=['jpg'])
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    if st.button('CAPTURE IMAGE'):
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        RGB_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #FRAME_WINDOW.image(frame)
        st.write('Captured Image')
        st.image(frame , width=250, height=250,channels='RGB')
        cv2.imwrite('filename.jpg', RGB_img)
    else:
        print('kartik op')

    input_name = st.text_input('Enter your full name')
    input_email = st.text_input('Email')
    input_age = st.text_input('Age')
    input_gender = st.text_input('Gender')
    karik_image = "filename.jpg"

    if image_file is not None:
       image_name = image_file.name
    else:
       image_name = "Not uploaded image"

       # save image and display on sidebar
    if image_file is not None:
        our_image = Image.open(image_file)
        saved = our_image.save('out.jpg')
        st.sidebar.write('Uploaded Image')
        st.sidebar.image(our_image , width=250, height=250,channels='RGB')

        #store data and images on firebase a
    if st.button('Submit'):
        st.success('Your response was registered')     
        storage.child(str(uuid.uuid4())).put("filename.jpg")
        storage.child(image_name).put('out.jpg')
        #image_url = storage.child(image_name).get_url(image_name)
        data = {"image_name":image_name , "user_name":input_name , "user_email":input_email, "user_age":input_age , "user_gender":input_gender,'image_name':image_name,"q1_a": option, "q2_a":option2 , "q3_a":option3 , "q4_a":option4,"q5_a":option5}
        db.child("Responses").push(data)

        # html to hide footer and menu
        hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
		.reportview-container .main footer {visibility: hidden;}  
        </style>
        """
        st.markdown(hide_menu_style, unsafe_allow_html=True)

    if st.button('Next'):
        webbrowser.open_new_tab(url)
       
if __name__ == '_main_':
    main()