<template>
    <div class="modal" id="login" tabindex="-1" aria-labelledby="loginLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable loginStyle">
            <div class="modal-content">
                <div class="Step">
                    <div class="Art Step__art"></div>
                    <div class="LoginContent">
                        <div class="LoginForm">
                            <h1 class="Title m-no-margin">Login</h1>
                            <p class="UserAgreement" >
                                By continuing, you agree to our 
                                <a target="_blank" href="https://www.redditinc.com/policies/user-agreement">User Agreement</a>
                                and 
                                <a target="_blank" href="https://www.redditinc.com/policies/privacy-policy">Privacy Policy.</a>
                            </p>
                            <div class="CreateAccWithSso">
                                <div id="with-google" class="Sso__button Sso__googleIdButton">
                                    Continue with Google
                                </div>
                                <div id="with-google" class="Sso__button Sso__appleIdContainer">
                                    Continue with VK
                                </div>
                                <div class="Sso__divider">
                                    <span class="Sso__dividerLine"></span>
                                    <span class="Sso__dividerText">or</span>
                                    <span class="Sso__dividerLine"></span>
                                </div>
                            </div>
                            <div class="AnimatedForm__errorMessage" v-if="isLoginError">Incorrect Username or Password</div>
                            <fieldset class="AnimatedForm__field m-required login hideable" >
                                <input id="loginUsername" class="AnimatedForm__textInput " style="font-size: 16px" type="text" name="username"  data-empty="false" v-model="username">
                                <label class="AnimatedForm__textInputLabel " for="loginUsername">Username</label>
                            </fieldset>
                            <fieldset class="AnimatedForm__field m-required password hideable m-small-margin">
                                <input id="loginPassword" class="AnimatedForm__textInput " type="password" name="password" data-empty="true" v-model="password">
                                <label class="AnimatedForm__textInputLabel " for="loginPassword">Password</label>
                            </fieldset>
                            <fieldset class="AnimatedForm__field m-small-margin">
                                <button class="AnimatedForm__submitButton m-full-width" href='/' @click="login">Log In</button>
                                <div class="AnimatedForm__submitStatus">
                                    <div class="AnimatedForm__submitStatusIcon"></div>
                                    <span class="AnimatedForm__submitStatusMessage"></span>
                                </div>
                            </fieldset>
                            <div class="BottomText m-secondary-text login-bottom-text hideable">
                                <span class="BottomLink m-secondary-text">Forgot your</span> <a class="BottomLink m-secondary-text" href="/">username</a> <span class="BottomLink m-secondary-text">or</span> <a class="BottomLink m-secondary-text" href="/">password</a><span class="BottomLink m-secondary-text m-question">&nbsp;?</span>
                            </div>
                            <div class="BottomText login-bottom-text register hideable">New to Moiras?
                                <a class="BottomLink" href="/signup">Sign up</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import axios from 'axios';
const AUTH_REQUEST ="http://127.0.0.1:8000/auth/token/"

export default {
    name: 'Login',
    data(){
        return{
            username:'',
            password:'',
            isLoginError:false
        }
    },
    methods: {
        login() {
            const {username,password} = this
            console.log(username,password)
            axios.post(AUTH_REQUEST + 'login', {
                username,password
                }).then(response => {
                    localStorage.clear()
                    localStorage.setItem('token', JSON.stringify(response.data.auth_token));
                    location.reload()
                }).catch(err=>{
                    console.log(err)
                    this.isLoginError = true
                });
        }
    }
}
</script>


<style scoped>
@import "../assets/static/assets/css/oneui.min.css";
.Art {
    background-image: url(https://www.redditstatic.com/accountmanager/bbb584033aa89e39bad69436c504c9bd.png);
    height: 100vh;
    min-height: 430px;
    background-repeat: no-repeat;
    background-size: cover;
}
.Step__art {
    width: 156px;
}
.loginStyle{
    width: 2000px;
}
.modal-dialog{
    max-width: 850px;
}
.Step {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -ms-flex-flow: row nowrap;
    flex-flow: row nowrap;
    
}
.LoginForm{
    width: 280px;
}
.LoginContent{
    align-self: center;
    padding: 24px;
    width: 100%;
    height: 100%;
}
.Title.m-no-margin {
    margin: 0;
}
.Title {
    font-size: 18px;
    font-weight: 500;
    line-height: 22px;
    margin: 20px 0;
}
.UserAgreement {
    margin-bottom: 48px;
    font-family: Noto Sans,sans-serif;
    font-size: 12px;
    font-weight: 400;
    line-height: 18px;
    margin-top: 8px;
}
.CreateAccWithSso{
    margin-bottom: 18px;

}
.Sso__button{
    font-family: IBMPlexSans,sans-serif;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: .5px;
    line-height: 32px;
    color: #fff;
    display: inline-block;
    border: none;
    border-radius: 4px;
    text-align: center;
    background: #0079d3;
    text-transform: uppercase;
    cursor: pointer;
    line-height: unset;
    min-height: 35px;
    max-width: 392px;
    width: auto;
    min-width: 155px;
    padding: 5px 10px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    background-color: #fff;
    color: #0079d3;
    border: 1px solid #0079d3;
    display: block;
    height: auto;
    margin: 8px 0;
    padding: 12px 28px;
    width: 100%;
}
.Sso__googleIdButton{
    padding: 16px 0 16px 65px;
    position: relative;
    text-align: left;

}
.Sso__googleIdButton:before {
    background-color: #fff;
    border-radius: 3px;
    content: "";
    height: 46px;
    left: 2px;
    position: absolute;
    top: 2px;
    width: 46px;
}
.Sso__googleIdButton:after {
    background-repeat: no-repeat;
    content: "";
    height: 20px;
    left: 16px;
    position: absolute;
    width: 20px;
    background-image: url(https://www.redditstatic.com/accountmanager/021031274726bcaef27a190f609eb59f.svg);
}
.Sso__appleIdContainer {
    padding: 16px 0 16px 65px;
    text-align: left;
    position: relative;
}
.Sso__appleIdContainer:before {
    background-color: #fff;
    border-radius: 3px;
    content: "";
    height: 46px;
    left: 2px;
    position: absolute;
    top: 2px;
    width: 46px;
}
.Sso__appleIdContainer:after {
    background-repeat: no-repeat;
    content: "";
    height: 20px;
    left: 16px;
    position: absolute;
    width: 20px;
    background-image: url(https://www.redditstatic.com/accountmanager/56133cfff407f8c1fb8694b4ef00975c.svg);
    bottom: 15px;
}
.Sso__divider {
    -webkit-box-align: center;
    align-items: center;
    display: flex;
    margin: 28px 0;
    -webkit-box-pack: justify;
    justify-content: space-between;
}
.Sso__dividerLine {
    border-top: 1px solid #edeff1;
    width: 40%;
}
.Sso__dividerText {
    font-size: 14px;
    font-weight: 500;
    line-height: 18px;
    color: #878a8c;
    text-transform: uppercase;
}
.AnimatedForm__field {
    position: relative;
}
fieldset {
    border: none;
    margin: 0;
    padding: 0;
}
fieldset {
    display: block;
    margin-inline-start: 2px;
    margin-inline-end: 2px;
    padding-block-start: 0.35em;
    padding-block-end: 0.625em;
    min-inline-size: min-content;
}
.AnimatedForm__field.m-valid .AnimatedForm__textInput {
    padding-right: 36px;
    border-color: #24a0ed;
}
.AnimatedForm__textInput {
    transform: translateZ(0);
    outline: 0;
    width: 100%;
    appearance: none;
    transition: all .2s ease-in-out;
    height: 48px;
    padding: 22px 12px 10px;
    border: 1px solid rgba(0,0,0,.1);
    border-radius: 4px;
    background-color: #fcfcfb;
}
input{
    -webkit-writing-mode: horizontal-tb !important;
    text-rendering: auto;
    color: -internal-light-dark(black, white);
    letter-spacing: normal;
    word-spacing: normal;
    text-transform: none;
    text-indent: 0px;
    text-shadow: none;
    display: inline-block;
    text-align: start;
    -webkit-rtl-ordering: logical;
    cursor: text;
    font: 400 13.3333px Aria
}
.AnimatedForm__textInputLabel {
    font-size: 8.7px;
    font-weight: 600;
    letter-spacing: .5px;
    position: absolute;
    display: inline-block;
    vertical-align: middle;
    top: 5px;
    left: 12px;
    color: #a5a4a4;
    text-transform: uppercase;
    transform: translateZ(0);
    transform-origin: 0 50%;
    transition: all .2s ease-in-out;
    pointer-events: none;
    line-height: 23px;
}
label {
    cursor: default;
}

.AnimatedForm__errorMessage {
    font-size: 12px;
    font-weight: 600;
    line-height: 16px;
    margin-top: -5px;
    margin-left: 65px;
    max-height: 1000px;
    opacity: 1;
    color: #ea0027;
    transition: .2s ;
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
    width: 100%;
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
    min-width: 155px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.AnimatedForm__submitStatusMessage {
    display: table-cell;
}

.BottomText {
    font-family: Noto Sans,sans-serif;
    font-size: 12px;
    font-weight: 400;
    line-height: 18px;
    margin-top: 8px;
    margin-bottom: 20px;
}
.BottomText .BottomLink.m-secondary-text {
    font-weight: 400;
    text-transform: none;
}
.BottomText .BottomLink {
    font-family: IBMPlexSans,sans-serif;
    font-size: 12px;
    letter-spacing: .5px;
    line-height: 24px;
}
.BottomLink.m-question {
    margin-left: -2px;
}
.BottomText {
    font-family: Noto Sans,sans-serif;
    font-size: 12px;
    font-weight: 400;
    line-height: 18px;
    margin-top: 8px;
    margin-bottom: 20px;
}
</style>
