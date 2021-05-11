<template>
  <div >
    <p class="today">Trending today</p>
    <div class="row">
        <div class="col-6 col-md-3 col-lg-6 col-xl-3 " v-for="item in trendingToday.trendingToday" :key="item.id" >
            <a class="block block-rounded block-link-pop" href="javascript:void(0)">
                <div class="block-content block-content-full">
                    <h4 class="font-w400 marginforNAme">
                        {{truncate(item.title,20)}}
                    </h4> 
                    <div class="font-size-h6 font-w400 text-dark">
                        {{truncate(item.content,40)}}
                    </div>
                    <span class="nik">
                        {{truncate(item.nik,30)}}
                    </span>
                </div>
            </a>
        </div>
        <div class="timeline-event-block block postBlok"  data-toggle="appear" v-for="item in defaultPosts.defaultPosts" :key="item.id">
            <div class="block-header">
                <h3 class="block-title">{{item.nik}}</h3>
                <div class="block-options">
                    <div class="timeline-event-time block-options-item font-size-sm">
                        {{item.createdDate}}
                    </div>
                    <div class="timeline-event-time block-options-item font-size-sm">
                        Rating: {{item.rating}}
                    </div>
                </div>
            </div>
            <div class="block-content">
                <p class="font-w600 mb-2">
                    {{item.title}}
                </p>
                <p v-html="item.content"></p>
            </div>
        </div>
    </div>
    <Login/>
    <SignUp/>
  </div>
</template>

<script>

import axios from 'axios';
import Login from '../components/Login.vue';
import SignUp from '../components/SignUp.vue';
const API = 'http://127.0.0.1:8000/moiras/posts';
// const defaultPost = '/default-posts';
// const imagePost = '/image-posts';
const urlPost = '/url-posts';

export default {
    name: 'Main',
    components:{Login,SignUp},
    data() {
        return {

            trendingToday:{
                trendingToday: [
                ]
            },
            defaultPosts:{
                defaultPosts: [
                ]
            }
        }
    },
    mounted(){
        console.log('hello world');
        this.trending_today()
        this.getPosts()
    },
    methods:{
        getPosts() {
            axios({
                method: 'GET',
                url: 'http://127.0.0.1:8000/moiras/posts/default-posts/', 
            }).then(response=> {
                console.log(response.data)
                for(var item of response.data){
                    console.log(item)

                    let authorName = this.getUserName(item.author);
                    console.log(this.getUserName(item.author))
                    this.defaultPosts.defaultPosts.push({
                        title:item.title,
                        content:item.content,
                        nik:authorName,
                        createdDate:item.created_at,
                        rating:item.rat_indicator,
                        })
                    console.log(this.defaultPosts.defaultPosts)
                }
            });
        },

        getUserName(id){
            let authorName = '';
            axios.get("http://127.0.0.1:8000/moiras/posts/users/"+id+"/",{
            }).then(response => {
                authorName = response.data.username
                console.log(response.data.username)
            }).catch(err=>{
                console.log(err)
            });
            console.log(authorName)
            return authorName
        },

        trending_today() {
            let vue = this;
            axios({
                method: 'GET',
                url: API+urlPost+'/?ordering=rat_indicator&limit=4', 
            }).then(function(response) {
                console.log(response.data.results)
                for(var item of response.data.results){
                    console.log(item)
                    vue.trendingToday.trendingToday.push({content:item.title,title:item.aboutData,nik:String(item.author)})
                    console.log(vue.trendingToday.trendingToday)
                }
            });
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
.postBlok{
    width:100%;
    margin:30px 50px 10px 50px;
}
</style>
