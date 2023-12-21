// this file creates the router instance that is used by our application
// we start by importing the createRouter and createWebHistory functions, as well as the components describing each of our views
import { createRouter, createWebHistory } from "vue-router";
import { useAuth0 } from "@auth0/auth0-vue";
import { watchEffect, watch } from 'vue';

// General Pages
import Home from "../views/general/Home.vue";
import Callback from "../views/general/Callback.vue";
import Default from "../views/general/Default.vue";
import PostLogin from "../views/general/PostLogin.vue";
import PrivacyPolicy from "../views/general/PrivacyPolicy.vue";
import TermsOfService from "../views/general/TermsOfService.vue";

// Student Pages
import ManageCourses from "../views/student/ManageCourses.vue";
import Schedule from "../views/student/Schedule.vue";
import SearchCourses from "../views/student/SearchCourses.vue";
import ShoppingCart from "../views/student/ShoppingCart.vue";
import CourseInfo from "../views/student/CourseInfo.vue";

// Teacher pages
import TeacherManageCourses from "../views/professor/ManageCourses.vue"
import TeacherSchedule from "../views/professor/Schedule.vue"
import { useStore } from 'vuex';

const authGuard = (to, from, next) => {
  const { isAuthenticated, isLoading, loginWithRedirect, idTokenClaims } = useAuth0();
  const store = useStore();

  const guardAction = () => {
    if (isAuthenticated) {
      const role = idTokenClaims._rawValue['https://ss.com/roles'][0]
      store.commit('setRole', { role: role });
      return next();
    }

    loginWithRedirect({ appState: { target: '/postlogin' } });
  };

  if (isLoading.value) {
    watch(isLoading, (newIsLoading) => {
      if (!newIsLoading) {
        guardAction();
      }
    });
  } else {
    guardAction();
  }
};

const router = createRouter({
  // the history mode determines how vue router interacts with the url.
  // createWebHistory() simulates the default browser behavior of changing
  // the path of the url based on the current document.
  // import.meta.env.BASE_URL is a vite feature that you don't need to worry about
  // and can safely use. it refers to the current path to the directory being
  // served by vite, which in this project is always the same directory
  // (and therefore import.meta.env.BASE_URL is '/')
  history: createWebHistory(import.meta.env.BASE_URL),

  // each entry to this routes array has a path (what goes in the URL to access
  // this page), a name (check out components/AppHeader.vue for how this is used)
  // and, most importantly, the component that should be rendered for the view
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/callback",
      name: "callback",
      component: Callback,
    },
    {
      path: "/default",
      name: "default",
      component: Default,
    },
    {
      path: "/privacy",
      name: "privacy",
      component: PrivacyPolicy,
    },
    {
      path: "/terms",
      name: "terms",
      component: TermsOfService,
    },
    {
      path: "/postlogin",
      name: "postlogin",
      component: PostLogin,
      beforeEnter: authGuard
    },
    {
      path: "/managecourses",
      name: "managecourses",
      component: ManageCourses,
      beforeEnter: authGuard
    },
    {
      path: "/schedule",
      name: "schedule",
      component: Schedule,
      beforeEnter: authGuard
    },
    {
      path: "/searchcourses",
      name: "searchcourses",
      component: SearchCourses,
      beforeEnter: authGuard
    },
    {
      path: "/courseinfo",
      name: "courseinfo",
      component: CourseInfo,
      props: true, // Enable props
      beforeEnter: authGuard
    },
    {
      path: "/shoppingcart",
      name: "shoppingcart",
      component: ShoppingCart,
      beforeEnter: authGuard
    },
  ],
});

export default router;
