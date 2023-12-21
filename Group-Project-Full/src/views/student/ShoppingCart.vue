<template>
  <main class="shoppingcart">
    <div id="shopping-cart-table">
      <table>
        <thead>
          <tr>
            <th>Course</th>
            <th>Section</th>
            <th>Credit Hours</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, idx) in ShoppingCartCourses" :key="idx">
            <td>{{ item.cid }}</td>
            <td>{{ item.sec }}</td>
            <td>{{ item.course_data.creditHours }}</td>
            <td v-if="removingFromCart.length != 2 || removingFromCart[0] != item.cid || removingFromCart[1].toString() != item.sec">
              <button @click="removeSectionFromCart(item.cid, item.sec)">Remove</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <button id="enroll-all-btn" :class="{ 'showing': ShoppingCartCourses.length > 0 }" v-if="ShoppingCartCourses.length > 0" @click="enrollAllCourses()">
      Enroll all courses
    </button>
  </main>
</template>


<script setup>
import { ref, onMounted, watch } from 'vue';
import { useAuth0 } from '@auth0/auth0-vue';
import { getUserShoppingCart, removeFromCart, enrollCourses } from '@/util/apiCaller';
const { getAccessTokenSilently } = useAuth0();

const removingFromCart = ref([]);
const ShoppingCartCourses = ref([]);

// watch(ShoppingCartCourses, (newVal) => {
//   let enrollButton = document.getElementById('enroll-all-btn');
//   if (enrollButton) {
//     if (newVal.length > 0) {
//       enrollButton.addClass('showing');
//     } else {
//       enrollButton.removeClass('showing');
//     }
//   }
// }, { deep: true });

const enrollAllCourses = async () => {
  try {
    console.log("Enrolling Courses");
    console.log("Updating user cart");
    const accessToken = await getAccessTokenSilently();
    await enrollCourses(accessToken);
    ShoppingCartCourses = updateUserCart();
  } catch (error) {
    console.error("Failed to fetch user cart:", error);
  }
}

const updateUserCart = async () => {
  try {
    console.log("Updating user cart");
    const accessToken = await getAccessTokenSilently();
    const resp = await getUserShoppingCart(accessToken);
    ShoppingCartCourses.value = resp.data.items;
  } catch (error) {
    console.error("Failed to fetch user cart:", error);
  }
}

const removeSectionFromCart = async (cid, section) => {
  try {
        console.log(cid);
        removingFromCart.value = [cid, section];
        const accessToken = await getAccessTokenSilently();

        await removeFromCart(cid, section, accessToken);
        console.log("Course remoWved from cart successfully");
        await updateUserCart();
        removingFromCart.value = [];
    } catch (error) {
        console.error("Failed to add course:", error);
        removingFromCart.value = [];
        // Handle error appropriately
    }
}


onMounted(async () => {
  await updateUserCart();
  console.log(ShoppingCartCourses);
});
  
</script>

<style>

#shopping-cart {
  position: relative;
}

#enroll-all-btn {
  position: absolute;
  right: calc(50% - 10rem);
  bottom: 0rem;
  margin-bottom: 3rem;
  width: 10rem;
  height: 3rem;
  background-color: var(--accent-orange);
  color:black;
  border-radius: 0.25rem;
  filter: drop-shadow(0rem 0px 2px var(--accent-grey));
  transition: margin-bottom 0.7s ease;
}

.showing {
  margin-bottom: 3rem;
}

#enroll-all-btn:hover {
  background-color: var(--accent-orange-hover);
}
/* make the heading font larger and add spacing below */

#shopping-cart-table { 
  position: relative;
  overflow-y: auto; 
  height: 100%; 
} 

#shopping-cart-table thead th { 
  position: sticky; 
  top: 0; 
} 


#shopping-cart-table table {
  margin-top: 0rem;
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;  /* Remove spacing between cells */
  border-radius: 0.25rem;
}

#shopping-cart-table td {
  padding: 0.5rem;
  height: 4rem;
  text-align: left;
  border-bottom: 1px solid #ddd;  /* Add border to the left of cells */
  color:black;
}
#shopping-cart-table th { 
  padding: 0.25rem;
  text-align: left;
  border-bottom: 0.1rem solid var(--sidebar);
  color: white;
  background: var(--primary-blue);
}

#shopping-cart-table th:first-child {
    border-top-left-radius: 0.25rem;
}

#shopping-cart-table th:last-child {
    border-top-right-radius: 0.25rem;
}

#shopping-cart-table button {
  color:white;
  border-radius: 1rem;
  height: 2.5rem;
  width: 6rem;
  margin-left: 1rem;
  position: center;
  background:var(--accent-red);
}

#shopping-cart-table button:hover {
    background-color: #0056b3;
}

</style> 