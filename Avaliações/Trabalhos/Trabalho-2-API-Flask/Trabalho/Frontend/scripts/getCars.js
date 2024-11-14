async function fetchCars() {
    try {
        // const accessToken = localStorage.getItem("token");
        const accessToken = getCookie("token");
        const response = await fetch('http://localhost:5000/cars', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${accessToken}`
            }
        });
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
        const data = await response.json();

        const tableBody = document.getElementById('carsTableBody')
        tableBody.innerHTML = '';

        data.forEach((client, index) => {
            const row = document.createElement('tr');

            const idCell = document.createElement('td');
            idCell.textContent = client.id;

            const nameCell = document.createElement('td');
            nameCell.textContent = client.name;

            const priceCell = document.createElement('td');
            priceCell.textContent = client.price;

            row.appendChild(idCell);
            row.appendChild(nameCell);
            row.appendChild(priceCell);

            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Error fetching client data:', error);
    }
}

window.onload = fetchCars;