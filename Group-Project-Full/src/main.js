import { createAuth0, useAuth0 } from "@auth0/auth0-vue";
import Vuex from 'vuex';
import { createStore } from 'vuex'
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./assets/main.css";

const app = createApp(App);

// router.beforeEach(async (to, from, next) => {
//     const { isAuthenticated } = useAuth0();
  
//     // Check if the user is authenticated
//     if (isAuthenticated) {
//       if (to.path !== '/postlogin' && to.path !== '/logout' && to.path !== '/') {
//         // Redirect to '/postlogin' if the user is authenticated and not already on that page
//         return next({ path: '/postlogin' });
//       }
//     }
  
//     next();
//   });

const store = createStore({
    state () {
      return {
        userVerified: false,
        userRole: 'Default'
      }
    },
    mutations: {
      verify (state) {
        state.userVerified = true
      },
      setRole (state, { role }) {
        state.userRole = role
      }
    }
  })

//Define global custom directives
app.directive('on-click-outside', {
    // Checks if a click was outside the element that has this directive.
    // The directive also ignores elements with the 'ignore-click-outside' class
    beforeMount(el, binding, vnode) { // Runs when the directive is attached to an element
        el.clickOutsideEvent = function (event) {
            if (!(el === event.target || el.contains(event.target) || event.target.closest(".ignore-click-outside"))) { // If the clicked element was not the target or its children or does not contain the ignore class
                vnode.ctx.exposed[binding.value.name](event); // call the function binding
            }
        };
        document.body.addEventListener('click', el.clickOutsideEvent);
    },
    beforeUnmount(el) { // Runs when the element is destroyed and removes the 'click' event listener
        document.body.removeEventListener('click', el.clickOutsideEvent);
    }
});


app
    .use(router)
    // .use(Vuex)
    .use(store)
    // define an instance of the authentication plugin from the Auth0 Vue SDK using the configuration values from the Auth0 application in the Auth0 Dashboard: Auth0 Domain and Client ID.
    .use(
        createAuth0({
            domain: import.meta.env.VITE_AUTH0_DOMAIN,
            clientId: import.meta.env.VITE_AUTH0_CLIENT_ID,   
            // Use the authorizationParams configuration object to define the query parameters that Vue needs to include on its calls to the Auth0 /authorize endpoint. 
            // Define the redirect_uri property within this object to specify the URL from your Vue.js application to where Auth0 should redirect your users after they successfully log in.
            authorizationParams: {
                audience: import.meta.env.VITE_AUTH0_AUDIENCE,
                redirect_uri: import.meta.env.VITE_AUTH0_CALLBACK_URL
            },
            scope: "openid profile email"
        })
    )
    .mount("#app");


