import axios from "axios";

/**
 * Get bearer token for Auth0 management API. 
 * Used for authenticating 
 *  - AddAuth0UserRoles
 *  - removeAuth0UserRoles
 */
async function getAuth0ManagementToken() {
    return axios.post(`${import.meta.env.VITE_AUTH0_MANAGEMENT_API_TOKEN_URL}`, 
    { // Body
        client_id: `${import.meta.env.VITE_AUTH0_MANAGEMENT_CLIENT_ID}`,
        client_secret: `${import.meta.env.VITE_AUTH0_MANAGEMENT_CLIENT_SECRET}`,
        audience: `${import.meta.env.VITE_AUTH0_MANAGEMENT_API_URL}`,
        grant_type: 'client_credentials',
        'Access-Control-Allow-Origin': '*' 
    }, 
    {
        headers: {
            'Content-Type': 'application/json',
        }
    });
}

// Create a new AWS user in the DynamoDB database
export const createAWSUser = async (uid, token) => {
    console.log("Creating AWS user")
    return axios.post(`${import.meta.env.VITE_API_SERVER_URL}users/post`, 
    { // Body   `
        uid: `${uid}`
    }, 
    {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });
}

// newRole must be int
export const addAuth0UserRoles = async (uid, roles) => {
    await getAuth0ManagementToken()
        .then(resp => {
            console.log(resp);
            axios.post(`${import.meta.env.VITE_AUTH0_MANAGEMENT_API_URL}users/${uid}/roles`, 
            { // Body
                roles: roles
            }, 
            {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${resp.data.access_token}`
                }
            });
        });
}

export const removeAuth0UserRoles = async (uid, roles) => {
    await getAuth0ManagementToken()
        .then(resp => {
            console.log(resp);
            axios.delete(`${import.meta.env.VITE_AUTH0_MANAGEMENT_API_URL}users/${uid}/roles`, 
            { // Body
                roles: roles
            }, 
            {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${resp.data.access_token}`
                }
            });
        });
}

export const getUser = async (token) => {
    const resp = await axios.get(`${import.meta.env.VITE_API_SERVER_URL}users/get`, 
    {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });
    return resp;
}

// Returns all courses a user is registered to
export const getUserCourses = async (format, token) => {
    const resp = await axios.get(`${import.meta.env.VITE_API_SERVER_URL}users/getEnrolled?format=${format}`,
    {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });
    return resp;
}

// Returns all courses in users shopping cart
export const getUserShoppingCart = async (token) => {
    const resp = await axios.get(`${import.meta.env.VITE_API_SERVER_URL}users/getCart`, 
    {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });
    return resp;
}

export const addToCart = async (cid, section, token) => {
    const resp = await axios.post(`${import.meta.env.VITE_API_SERVER_URL}users/addToCart`, 
    {
        cid: cid.value,
        section: section
    },
    {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });
    return resp;
}

export const removeFromCart = async (cid, section, token) => {
    console.log(`Attempting to remove course ${cid} with section ${section}`);
    console.log(cid);
    const resp = await axios.post(`${import.meta.env.VITE_API_SERVER_URL}users/removeFromCart`, 
    {
        cid: cid,
        section: section
    },
    {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });
    return resp;
}

export const enrollCourses = async (token) => {
    const resp = await axios.get(`${import.meta.env.VITE_API_SERVER_URL}users/enrollCart`, 
    {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });
    return resp;
}

// Returns generic course info and a list of the courses' sections and their info
export const getCourseInfo = async (courseId, token) => {
    return axios.get(`${import.meta.env.VITE_API_SERVER_URL}sections/get`,
    {
        "cid": courseId
    }, 
    { // Headers
        'Content-Type': 'application/json', // Assuming you're sending JSON data
        'Authorization': `Bearer ${token}`,
    });
}

export const getCourseSections = async (courseId, token) => {
    const resp = await axios.get(`${import.meta.env.VITE_API_SERVER_URL}courses/getSections?cid=${courseId}`,
    {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });
    return resp;
}

export const searchCourses = async (searchQuery, token) => {
    const resp = await axios.get(`${import.meta.env.VITE_API_SERVER_URL}courses/search?searchQuery=${searchQuery}`,
    {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });
    return resp;
}


