document.getElementById('registerSale').addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    // Get form data
    const name = document.getElementById('name').value;
    const car = document.getElementById('car').value;
    const dealer = document.getElementById('dealer').value;
    const price = document.getElementById('price').value;

    // Prepare the data to be sent in the request body
    const data = {
        name: name,
        car: car,
        dealer: dealer,
        price: price
    };

    try {
        // Send a POST request to the server
        const accessToken = getCookie("token");
        const response = await fetch('http://localhost:5000/registersale', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${accessToken}`
            },
            body: JSON.stringify(data)
        });

        document.getElementById('registerSale').reset();

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
        document.getElementById('registerSale').reset();
        window.location.reload(true);

    }
});