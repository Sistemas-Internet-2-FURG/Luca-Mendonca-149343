async function fetchSales() {
    try {
        const accessToken = getCookie("token");
        const response = await fetch('http://localhost:5000/sales', {
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

        const tableBody = document.getElementById('salesTableBody')
        tableBody.innerHTML = '';

        data.forEach((client, index) => {
            const row = document.createElement('tr');

            const idCell = document.createElement('td');
            idCell.textContent = client.id;

            const clientCell = document.createElement('td');
            clientCell.textContent = client.client;

            const dealerCell = document.createElement('td');
            dealerCell.textContent = client.dealer;

            const carCell = document.createElement('td');
            carCell.textContent = client.car;

            const priceCell = document.createElement('td');
            priceCell.textContent = client.price;

            const actionCell = document.createElement('td');

            const form = document.createElement('form');
            form.id = 'removeSale';
            form.onsubmit = (event) => removeSale(event, client.id);

            const idInput = document.createElement('input');
            idInput.type = 'hidden';
            idInput.name = 'id';
            idInput.value = client.id;
            idInput.id = 'saleId';

            const formGroup = document.createElement('div');
            formGroup.className = 'form-group';

            const submitButton = document.createElement('button');
            submitButton.type = 'submit';
            submitButton.textContent = 'Remover';

            formGroup.appendChild(submitButton)

            form.appendChild(idInput);
            form.appendChild(formGroup);

            actionCell.appendChild(form);

            row.appendChild(idCell);
            row.appendChild(clientCell);
            row.appendChild(dealerCell);
            row.appendChild(carCell);
            row.appendChild(priceCell);
            row.appendChild(actionCell);

            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Error fetching client data:', error);
    }
}

async function removeSale(event, id) {
    event.preventDefault(); // Prevent the default form submission behavior

    // const id = document.getElementById('saleId').value;

    const data = {
        id: id
    };

    try {
        const accessToken = getCookie("token");
        const response = await fetch(`http://localhost:5000/deletesale`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${accessToken}`
        },
        body: JSON.stringify(data)
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
        window.location.reload(true);
    } catch (SyntaxError) {
        window.location.reload(true);
    }
}

window.onload = fetchSales;