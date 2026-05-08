async function sendMail() {

    const email = document.getElementById("email").value;

    const status = document.getElementById("status");

    status.innerText = "Sending...";

    try {

        const response = await fetch(
            "https://automate-emails-backend.onrender.com/api/send/",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    email: email
                })
            }
        );

        const data = await response.json();

        status.innerText = data.message;

    } catch (error) {

        status.innerText = "Server Error";

    }
}