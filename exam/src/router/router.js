import { createWebHistory, createRouter } from "vue-router";
import Main from '../views/Main'
import Login from '../components/Login'

const routes = [
    {
      path: "/",
      name: "Main",
      component: Main,
    },
    {
      path: "/login",
      name: "Login",
      component: Login,
    },
  ];
  
const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;