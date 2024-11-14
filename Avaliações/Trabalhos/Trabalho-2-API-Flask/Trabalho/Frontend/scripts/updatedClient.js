document.getElementById('updateClientForm').addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    // Get form data
    const name = document.getElementById('name2').value;
    const email = document.getElementById('email2').value;
    const phone = document.getElementById('phone2').value;

    // Prepare the data to be sent in the request body
    const data = {
        name: name,
        email: email,
        phone: phone
    };

    try {
        // Send a POST request to the server
        const accessToken = getCookie("token");
        const response = await fetch('http://localhost:5000/updateclient', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${accessToken}`
            },
            body: JSON.stringify(data)
        });

        document.getElementById('updateClientForm').reset();

        if (!response.ok) {
            if (response.status === 401) {
                const errorData = await response.json();
                if (errorData.msg === "Token has expired") {
                    alert("Login expired, please login again.");
                    window.location.href = 'http://127.0.0.1:5500/login.html';
                    return;
                }
            }
            throw new Error('Network response was not ok ' + response.statusText);
        }

        window.location.reload(true);
    } catch (SyntaxError) {
        document.getElementById('updateClientForm').reset();
        window.location.reload(true);
    }
});