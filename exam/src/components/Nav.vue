<template>
  <div class="bg-white push navstyle">
    <!-- Toggle Navigation -->
    <div class="d-lg-none">
        <!-- Class Toggle, functionality initialized in Helpers.coreToggleClass() -->
        <button type="button" class="btn btn-block btn-light d-flex justify-content-between align-items-center" data-toggle="class-toggle" data-target="#horizontal-navigation-hover-normal" data-class="d-none">
            Menu - Hover Normal
            <i class="fa fa-bars"></i>
        </button>
    </div>
    <!-- END Toggle Navigation -->

    <!-- Navigation -->
    <div id="horizontal-navigation-hover-normal" class="d-none d-lg-block mt-2 mt-lg-0">
        <ul class="nav-main nav-main-horizontal nav-main-hover" v-if="!isUserAuth">
            <li class="nav-main-item headder">
                <a class="nav-main-link active homelink" href="/">
                    <i class="nav-main-link-icon fa fa-home"></i>
                    <span class="nav-main-link-name">moiras</span>
                </a>
            </li>

            <li class="nav-main-item widthSerach">
               <form class="d-none d-sm-inline-block search searchHiht" action="be_pages_generic_search.html" method="POST">
                    <div class="input-group input-group-sm searchHiht">
                        <div class="input-group-append searchHiht">
                            <span class="input-group-text  border-0 ">
                                <i class="si si-magnifier "></i>
                            </span>
                        </div>
                        <input type="text" class="form-control form-control-alt " placeholder="Search.." id="page-header-search-input2" name="page-header-search-input2">
                    </div>
                </form>
            </li>
            <button type="button" class="btn btn-outline-primary js-click-ripple-enabled reg-btn"  style="overflow: hidden; position: relative; z-index: 1;" data-toggle="modal" data-target="#login">Log In</button>
            <button type="button" class="btn btn-primary js-click-ripple-enabled reg-btn" style="overflow: hidden; position: relative; z-index: 1;" data-toggle="modal" data-target="#sign">Sign Up</button>
            <li class="nav-main-item ">
                <a class="nav-main-link nav-main-link-submenu settingsmy" data-toggle="submenu" aria-haspopup="true" aria-expanded="false" href="#">
                    <i class="nav-main-link-icon fa fa-user userlink"></i>
                </a>
                <ul class="nav-main-submenu">
                    <li class="nav-main-item">
                        <a class="nav-main-link" href="javascript:void(0)">
                            <span class="nav-main-link-name">Night mode</span>
                        </a>
                    </li>
                    <li class="nav-main-item">
                        <a class="nav-main-link" href="javascript:void(0)">
                            <span class="nav-main-link-name">Help</span>
                        </a>
                    </li>
                    <li class="nav-main-item">
                        <a class="nav-main-link" href="javascript:void(0)" data-toggle="modal" data-target="#login">
                            <span class="nav-main-link-name">Log In | Sign In</span>
                        </a>
                    </li>
                </ul>
            </li>
        </ul>
        <ul class="nav-main nav-main-horizontal nav-main-hover" v-else-if="isUserAuth">
            <li class="nav-main-item headder">
                <a class="nav-main-link active homelink" href="/">
                    <span class="nav-main-link-name">MOIRAS</span>
                </a>
            </li>
            <a class="nav-main-link active homelink currentPath">
                          <i class="nav-main-link-icon si si-home"></i>
                          <span class="nav-main-link-name">{{currentPage}}</span>
                        </a>
            <li class="nav-main-item widthSerachisAuth">
               <form class="d-none d-sm-inline-block search authSearch searchHiht" action="be_pages_generic_search.html" method="POST">
                    <div class="input-group input-group-sm searchHiht">
                        <div class="input-group-append searchHiht">
                            <span class="input-group-text  border-0 ">
                                <i class="si si-magnifier "></i>
                            </span>
                        </div>
                        <input type="text" class="form-control form-control-alt " placeholder="Search.." id="page-header-search-input2" name="page-header-search-input2">
                        
                    </div>
                </form>
            </li>
            <button type="submit" class="btn btn-outline-primary js-click-ripple-enabled reg-btn"  style="overflow: hidden; position: relative; z-index: 1;" @click="$router.push('/create')">
            Create Post
            </button>
            <li class="nav-main-item ">
                <a class="nav-main-link nav-main-link-submenu settingsmy" data-toggle="submenu" aria-haspopup="true" aria-expanded="false" href="#">
                    <i class="nav-main-link-icon fa fa-address-card userlink"></i>
                    <span>{{username}}</span>
                </a>
                <ul class="nav-main-submenu" style="background-color:white">
                    <li class="nav-main-item">
                        <a class="nav-main-link" href="javascript:void(0)">
                            <i class="nav-main-link-icon fa fa-user userlink"></i>
                            <span class="nav-main-link-name">Profile</span>
                        </a>
                    </li>
                    <li class="nav-main-item">
                        <a class="nav-main-link" href="javascript:void(0)">
                            <i class="nav-main-link-icon si si-settings userlink"></i>
                            <span class="nav-main-link-name">User Settings</span>
                        </a>
                    </li>
                    <li class="nav-main-item">
                        <a class="nav-main-link" href="javascript:void(0)">
                            <i class="nav-main-link-icon far fa-question-circle userlink"></i>
                            <span class="nav-main-link-name">Help Center</span>
                        </a>
                    </li>
                    <li class="nav-main-item">
                        <a class="nav-main-link" href="javascript:void(0)" @click="logOut_user">
                            <i class="nav-main-link-icon si si-logout userlink"></i>
                            <span class="nav-main-link-name">Log Out</span>
                        </a>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
    <!-- END Navigation -->
  </div>
</template>

<script>
import axios from 'axios';
const GET_ME_REQUEST = "http://127.0.0.1:8000/auth/users/me/"
const LOGUT_ME_REQUEST = "http://127.0.0.1:8000/auth/token/logout"
export default {
  name: 'Nav',
  components:{},
    data(){
        return{
           isUserAuth:false,
           username:'',
           email:'',
           currentPage:this.getPath(),
           currentIcon:this.getPath().toLowerCase(),
        }
    },
    mounted(){
      this.auth_user()
      console.log('hello world');
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
                }).catch(err=>{
                  console.log(err)
                });
            }
        },
        logOut_user() {
            axios.post(LOGUT_ME_REQUEST , {
                  headers: {
                    'Authorization': 'Token '+localStorage.getItem('token').replace(/"/g,''),
                  }
                }).then(response => {
                    console.log(response)
                    this.isUserAuth = false
                    this.username=''
                    this.email = ''
                }).catch(err=>{
                    location.reload()
                    localStorage.clear()
                    console.log(err)
                });
        },
        getPath(){
          let path = location.pathname
          if(path==='/'){
            path = 'Home'
          }
          return path
        },
        truncate(text, stop, clamp) {
            return text.slice(0, stop) + (stop < text.length ? clamp || '...' : '')
        },
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import "../assets/static/assets/css/oneui.min.css";
.homelink:hover{
 background-color: rgba(255, 255, 255, 0);
}
.navstyle{
  padding: 5px;
}
.userlink{
  color: rgb(138, 138, 138);
}
.nav-main-link{
    display: flex;
}
.reg-btn{
  display: inline;
  margin-right: 15px;
  border-radius: 17px;
  width: 120px;
  height: 100%;
}
.searchHiht{
  height: 100%;
  border-radius: 7px;
}
.search{
  width: 100%;
}
.input-group-sm>.custom-select, .input-group-sm>.form-control:not(textarea) {
  height: 100%;
}
.headder{
  margin-right: 100px;
}
.nav-main-horizontal>.nav-main-item:not(:last-child) {
  margin-right: 100px;
}
.widthSerach{
  width: 50%;
}
.widthSerachisAuth{
  width: 35%;
}
.currentPath{
  width: 20%;
}
</style>
