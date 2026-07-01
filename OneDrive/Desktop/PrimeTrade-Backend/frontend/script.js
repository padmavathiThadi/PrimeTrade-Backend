const API_URL = "http://127.0.0.1:8000";

async function register() {

    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch(`${API_URL}/register`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username,
            email,
            password
        })
    });

    const data = await response.json();

    alert(data.message);

    if(response.ok){
        window.location.href = "login.html";
    }
}
async function login() {

    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;

    const response = await fetch(`${API_URL}/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email,
            password
        })
    });

    const data = await response.json();

    if(response.ok){

        localStorage.setItem("token", data.access_token);

        alert("Login Successful!");

        window.location.href = "dashboard.html";

    }else{

        alert(data.detail);

    }
}
async function createTask(){

    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;

    const response = await fetch(`${API_URL}/tasks`,{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            title,
            description
        })

    });

    const data = await response.json();

    alert(data.message);

}

async function loadTasks(){

    const response = await fetch(`${API_URL}/tasks`);

    const tasks = await response.json();

    let output="";

    tasks.forEach(task=>{

        output += `
        <hr>
        <h3>${task.title}</h3>
        <p>${task.description}</p>
        `;

    });

    document.getElementById("tasks").innerHTML = output;

}