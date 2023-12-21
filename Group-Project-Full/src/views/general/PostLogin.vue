<template>
</template>

<script setup> 
import { onMounted } from 'vue';
import { useAuth0 } from '@auth0/auth0-vue';
import { createAWSUser, getUser, addAuth0UserRoles } from '@/util/apiCaller'
import { useStore } from 'vuex';
import router from "../../router"

const store = useStore();
const { isAuthenticated, idTokenClaims, getAccessTokenSilently } = useAuth0();

onMounted(async () => {
    if (isAuthenticated && idTokenClaims !== undefined) {
        try {
            // Get user data from ID Token claims
            console.log("ID token claims valid.");
            const token = await getAccessTokenSilently();
            const email = idTokenClaims._rawValue['https://ss.com/email']
            const role = idTokenClaims._rawValue['https://ss.com/roles'][0]
            const uid = idTokenClaims._rawValue.sub;

            // Try to get the user info. If user does not exist in database, create a new user
            try {
                await getUser(token);
            } catch (error) {
                if (error.request.responseText.includes('User not found')) {
                console.info("User not found in DynamoDB database. Creating new user with 'Default' role...")
                await createAWSUser(email, token);
                await addAuth0UserRoles(uid, [`${import.meta.env.VITE_AUTH0_ROLE_DEFAULT}`]);
                }
            }

            // Store that the user is verified and exists in the database
            store.commit('verify');
            // Store the role of the user for use in displaying the sidebar
            store.commit('setRole', { role: role });

            console.log(store.state.userRole);
            // Redirect user to proper page based on role
            switch(store.state.userRole) {
                case 'Admin':
                    router.push('/admindashboard');
                    break;
                case 'Student':
                    router.push('/managecourses');
                    break;
                case 'Professor':
                    router.push('/managecourses');
                    break;
                default:
                    router.push('/default');
            }

        } catch (error) {
            console.error(`Error retrieving access token or claims: ${error}`)
        }
    }
})

// // Watch for ID claims to populate
// watch([claims], async ([newClaims]) => {
// // get roles and login count from id token if claims are not undefined (meaning they were successfully retrieved)
// if (newClaims !== undefined) {
//     console.log("Id Token Claims updated");
    
//     try {
//     const token = await getAccessTokenSilently();
//     const email = claims._rawValue['https://ss.com/email']
//     const uid = claims._rawValue.sub;
//     role.value = claims._rawValue['https://ss.com/roles'][0]

//     try {
//         await getUser(token);
//     } catch (error) {
//         if (error.request.responseText.includes('User not found') && (sessionStorage.getItem("firstUserCreated") === null)) {
//         console.info("User not found in DynamoDB database. Creating new user with 'Default' role...")
//         await createAWSUser(email, token);
//         await addAuth0UserRoles(uid, [`${import.meta.env.VITE_AUTH0_ROLE_DEFAULT}`]);
//         }
//     }
//     store.commit('verify');

//     } catch (error) {
//     console.error(`Error retrieving access token or claims: ${error}`)
//     }
// }
// });
</script>

<style>
</style>