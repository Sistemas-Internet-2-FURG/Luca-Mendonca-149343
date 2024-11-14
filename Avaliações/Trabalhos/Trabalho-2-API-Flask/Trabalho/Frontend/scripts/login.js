document.getElementById('loginform').addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    // Get form data
    const name = document.getElementById('name').value;
    const password = document.getElementById('password').value;

    // Prepare the data to be sent in the request body
    const data = {
        name: name,
        password: password
    };

    try {
        // Send a POST request to the server
        const response = await fetch('http://localhost:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        const responsedata =  await response.json();
        document.cookie = `token=${responsedata}`;
        // alert(responsedata);

        document.getElementById('loginform').reset();

        window.location.href = 'http://127.0.0.1:5500/clients.html';
    } catch (SyntaxError) {
        document.getElementById('loginform').reset();

        window.location.href = 'http://127.0.0.1:5500/clients.html';
    }
});