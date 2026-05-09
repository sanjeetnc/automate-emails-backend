async function sendEmails() {

    const resultDiv =
        document.getElementById("result");

    const loader =
        document.getElementById("loader");

    const button =
        document.getElementById("sendBtn");


    loader.classList.remove("hidden");

    resultDiv.innerHTML = "";

    button.disabled = true;

    button.classList.add("opacity-50");


    try {

        const response =
            await fetch('/send/');
                const data =
            await response.json();


        loader.classList.add("hidden");

        resultDiv.innerHTML = `
            <div class="
                bg-green-500/10
                border border-green-400/30
                rounded-2xl
                p-4
                text-green-300
                animate-pulse
            ">
                ✅ ${data.total_emails_sent} Emails Sent Successfully
            </div>
        `;

    }

    catch(error) {

        loader.classList.add("hidden");

        resultDiv.innerHTML = `
            <div class="
                bg-red-500/10
                border border-red-400/30
                rounded-2xl
                p-4
                text-red-300
            ">
                ❌ Error Sending Emails
            </div>
        `;

        console.log(error);
    }

    button.disabled = false;

    button.classList.remove("opacity-50");
}