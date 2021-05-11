<template>
  <div >
    <div class="row">
      <div class="postCreate">
          <div class="_1HWpiNu6dkOnZixxwDYTVJ">
            <div class="_3M6BmdyQcCEQZu-MylN14">Create Post</div>
          </div>
          <div class="linee"></div>
            <div class="btn-group" role="group" aria-label="Horizontal Outline Secondary">
              <button type="button" class="btn btn-outline-secondary">Post</button>
              <button type="button" class="btn btn-outline-secondary">Image Post</button>
              <button type="button" class="btn btn-outline-secondary">Url Post</button>
            </div>
          <div class="postCreateEditor" v-if="isPost">
            <input type="text" class="form-control postTitle" id="example-text-input" v-model="title" name="example-text-input"       placeholder="Title">
             <ckeditor :editor="editor" class="editorCK" v-model="editorData" :config="editorConfig"></ckeditor>
             <button class="AnimatedForm__submitButton Sing m-full-width" type="submit" @click="createDefaultPost">Post</button>
         </div>
          <div class="postCreateEditor" v-else-if="isImagePost">  
            <input type="text" class="form-control postTitle" id="example-text-input" name="example-text-input"       placeholder="Title">
         </div>
          <div class="postCreateEditor" v-else-if="isUrlPost">
            <input type="text" class="form-control postTitle" id="example-text-input" name="example-text-input"       placeholder="Title">
         </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
const GET_ME_REQUEST = "http://127.0.0.1:8000/auth/users/me/"
const CREATE_POST_REQUEST = "http://127.0.0.1:8000/moiras/posts/default-posts/"
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';

export default {
    name: 'Create',
    data(){
        return{
            
            isUserAuth:false,
            username:'',
            email:'',
            userId:0,
            isPost:true,
            isImagePost:false,
            isUrlPost:false,
            editor: ClassicEditor,
            editorData: '',
            editorConfig: {
                // The configuration of the editor.
            },
            title:'',
            image:'',
            url:'',
            
        }
    },
    created(){
      this.auth_user()
    },
    methods:{
        auth_user() {
          if(!(localStorage.getItem('token')===null)){
            axios.get(GET_ME_REQUEST , {
                  headers: {
                    'Authorization': 'Token '+localStorage.getItem('token').replace(/"/g,''),
                  }
                }).then(response => {
                    console.log(response)
                    this.isUserAuth = true
                    this.username = response.data.username
                    this.email = response.data.email
                    this.userId = response.data.id
                }).catch(err=>{
                  console.log(err)
                  this.isUserAuth = false
                  this.$router.push('/')
                });
          }
          else{
          this.isUserAuth = false
          this.$router.push('/')
          }
      },
      createDefaultPost(){
        axios({
                method: 'POST',
                url: CREATE_POST_REQUEST,
                headers: {
                  'Authorization': 'Token '+localStorage.getItem('token').replace(/"/g,''),
                },
                data: {
                  aboutData:this.title,
                  title:this.title,
                  content:this.editorData,
                  urlContent:this.url,
                  author:this.userId,
                }
                }).then(response => {
                    console.log(response)
                }).catch(err=>{
                  console.log(err)
                });
      }
   }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import "../assets/static/assets/css/oneui.min.css";
.today{
    margin-bottom: 10px;
}
.nik{
    font-size: 11px;
}
.marginforNAme{
    margin-top: 50px;
    margin-bottom: 0px;
}
._3M6BmdyQcCEQZu-MylN14 {
    font-size: 18px;
    font-weight: 500;
    line-height: 22px;
    margin-top:15px;
    margin-bottom:10px;
    color: var(--newCommunityTheme-bodyText);
    -ms-flex: 1;
    flex: 1;
}
.linee{
  width:100%;
  height:0.1px;
  margin-bottom:5px;
  background-color:	#ffffe6;
}
.postTitle{
  margin-top :30px;
  margin-bottom :5px;
}
.postCreateEditor{
  background-color:white;
  padding:10px;
  border-radius:8px;
}
.AnimatedForm__submitButton {
    font-family: Noto Sans,sans-serif;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: unset;
    line-height: 18px;
    text-transform: unset;
    background: #0079d3;
    border-radius: 999px;
    color: #fff;
    height: 40px;
    padding: 0 16px;
}
.AnimatedForm__submitButton.m-full-width {
    width: 30px;
}
.AnimatedForm__submitButton, .AnimatedForm__submitButton:before {
    transition: color .01s ease-in,text-indent .25s ease-in,opacity .25s ease-in;
}
.AnimatedForm__submitButton {
    position: relative;
    display: inline-block;
    border: none;
    text-align: center;
    cursor: pointer;
    min-height: 35px;
    max-width: 392px;
    min-width: 100px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    left:500px;
    margin-top:15px
}
</style>
