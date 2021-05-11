import { createApp } from 'vue'
import App from './App.vue'
import Create from './views/Create.vue'
import Main from './views/Main.vue'
import CKEditor from '@ckeditor/ckeditor5-vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import {createRouter,createWebHistory } from 'vue-router'
const routes = [
  { path: '/', component: Main },
  { path: '/create', component: Create },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})


const app = createApp(App)
app.use(router)
app.use(CKEditor)
app.mount('#app')
