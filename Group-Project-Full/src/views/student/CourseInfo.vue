<template>
    <main id="course-info">
        <div id="info-header">
            <div id="title-wrapper">
                <h1 style="display: inline-block">{{ cid }}</h1>
                <h2 style="display: inline-block">{{ title }}</h2>
            </div>
            <h2 id="course-desc" style="font-weight: bold;">Description</h2>
            <p>{{ desc }}</p>
            <h2 id="course-credits" style="font-weight: bold;">Credits</h2>
            <p>{{ creditHours }}</p>
            <h2 id="course-prerequisites" style="font-weight: bold;">Prerequisites</h2>
            <p>{{ preReqs }}</p>
        </div>
        <hr id="divider">
        <div id="course-openings">
            <table>
                <thead>
                <tr>
                    <th v-for="field in availableSectionFields" :key="field.key">{{ field.label }}</th>
                </tr>
                </thead>
                <tbody>
                <tr v-if="availableSections != null" v-for="(item, idx) in availableSections" :key="item.id + (existsInCart(idx) ? 'inCart' : 'notInCart')">
                    <td v-for="field in availableSectionFields" :key="field.key">
                        <template v-if="field.key === 'actions'">
                            <div class="course-actions">
                                <button class="already-in-cart-button action-button" v-if="currentUserCart && existsInCart(idx)">Already in Cart!</button>
                                <div class="action-button" v-else-if="addingToCart == idx">Adding to cart...</div>
                                <button class="add-to-cart-button action-button" v-else @click="addSectionToCart(idx)">Add to Cart</button>
                            </div>
                        </template> 
                        <template v-else>
                            {{ item[field.key] }}
                        </template>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </main>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRoute } from 'vue-router';
import { useAuth0 } from '@auth0/auth0-vue';
import { getCourseSections, addToCart, getUserShoppingCart } from '@/util/apiCaller';
const { getAccessTokenSilently } = useAuth0();

const addingToCart = ref(null);
// Get route for recieving route query parameters. e.g. /courseinfo?param=value
const route = useRoute();
const cid = ref(route.query.cid);
const title = ref(route.query.title);
const desc = ref(route.query.desc);
const creditHours = ref(route.query.creditHours);
const preReqs = ref(route.query.preReqs);

// General course data. This data will be descrbing the course based on the unique courseID 
const courseData = ref({});
const availableSections = ref([]);
const currentUserCart = ref([]);

const existsInCart = (idx) => {
    // Check if the section already exists in the cart
    return currentUserCart.value.items.some(item => item.cid == cid.value && item.sec == idx);
}

// Fields that describe each available course. Used as headers when rendering the available courses table
const availableSectionFields = ref([
    { key: 'status', label: 'Status' },
    { key: 'day', label: 'Meeting Dates' },
    { key: 'startTime', label: 'Meeting Time(s)' },
    { key: 'room', label: 'Room' },
    { key: 'professor', label: 'Instructor' },
    { key: 'rating', label: 'Rating' },
    { key: 'seats', label: 'Seats' },
    { key: 'actions', label: 'Actions' }  // Used for register button
]);

const updateUserCart = async () => {
    const accessToken = await getAccessTokenSilently();
    const resp = await getUserShoppingCart(accessToken);
    console.log(resp);
    currentUserCart.value = resp.data;
}

// Used to abort API queries if this Vue component is unmounted
const fetchSections = async () => {
    const accessToken = await getAccessTokenSilently();
    console.log(accessToken);
    const resp = await getCourseSections(cid.value.replace(/ /g, "+"), accessToken);
    availableSections.value = resp.data;
    console.log(availableSections.value);
    // availableSections = resp.data.items;
}

const addSectionToCart = async (section) => {
    try {
        addingToCart.value = section;
        const accessToken = await getAccessTokenSilently();

        await addToCart(cid, section, accessToken);
        console.log("Course added to cart successfully");
        await updateUserCart();
        addingToCart.value = null;
    } catch (error) {
        console.error("Failed to add course:", error);
        addingToCart.value = null;
        // Handle error appropriately
    }
}

onMounted(async () => {
    await updateUserCart();
    await fetchSections();
});
</script>


<style>

hr {
    margin-top: 0.1rem;
    margin-bottom: 0.1rem;
    height: 2px;
    background-color: black;
}

#divider {
    margin-top: 1rem;
    margin-bottom: 0rem;
    display: none;
}

#info-header {
    width: 100%;
    padding: 0rem;
}

#title-wrapper {
    background-color: var(--course-header);
    padding: 0.25rem;
    padding-left: 0.5rem;
    border-radius: 0.25rem;
}

#title-wrapper > h2 {
    margin-left: 1rem;
    color:white;
    font-size: 20px;
}

#title-wrapper > h1 {
    color:white;
    font-family: "Montserrat";
    font-size: 30px;
    font-weight: 700;
}  

#course-openings table {
    margin-top: 5rem;
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;  /* Remove spacing between cells */
    border-radius: 0.25rem;
    border-collapse: collapse;
    border-spacing:1rem;
}

#course-openings td {
    padding: 0.5rem;
    height: 4rem;
    text-align: left;
    border-bottom: 1px solid #ddd;  /* Add border to the left of cells */
    color:black;
}

#course-openings th {
    padding: 0.25rem;
    text-align: left;
    border-bottom: 0.1rem solid var(--accent-grey);
    color: var(--accent-grey);
}

#course-openings th:first-child {
    border-top-left-radius: 0.25rem;
}

#course-openings th:last-child {
    border-top-right-radius: 0.25rem;
}

.course-actions {
    display: flex;
    height: 100%;
}

.action-button {
    color:black;
    flex-grow: 1;
    border-radius: 0.25rem;
    filter: drop-shadow(0rem 0px 2px var(--accent-grey));
}

.register-button {
    background: var(--accent-b-orange);
}

.register-button:hover {
    background: var(--accent-b-orange-hover);
}

.add-to-cart-button {
    background: var(--accent-orange);
}

.add-to-cart-button:hover {
    background: var(--accent-orange-hover);
}

.already-in-cart-button {
    background: var(--accent-red);
    color: white;
}

.already-in-cart-button:hover {
    background: var(--accent-red);
    color: white;
    cursor: not-allowed;
}

</style>