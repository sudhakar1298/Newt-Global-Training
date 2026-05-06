<%@ taglib prefix="c" uri="jakarta.tags.core" %>

<!DOCTYPE html>
<html>

<head>

    <title>E-Commerce</title>

    <style>

        body {
            font-family: Arial;
            margin: 40px;

        }

        h1 {
            color: #333;
        }

        h2 {
            margin-top: 30px;
        }

        form {
            margin-bottom: 20px;
        }

        input {
            margin: 5px;
            padding: 8px;
        }

        button {
            padding: 8px 15px;
            cursor: pointer;
        }

        table {
            width: 80%;
            border-collapse: collapse;
            background-color: white;
        }

        table, th, td {
            border: 1px solid #ccc;
        }

        th {
            background-color: #ddd;
        }

        th, td {
            padding: 12px;
            text-align: center;
        }

    </style>

</head>

<body>

<h1>Product Store</h1>

<h2>Add Product</h2>

<form action="/products/add" method="post">

    <input type="text"
           name="name"
           placeholder="Product Name"
           required>

    <input type="number"
           step="0.01"
           name="price"
           placeholder="Price"
           required>

    <input type="number"
           name="quantity"
           placeholder="Quantity"
           required>

    <button type="submit">
        Add Product
    </button>

</form>

<h2>Available Products</h2>

<table>

    <tr>

        <th>ID</th>
        <th>Name</th>
        <th>Price</th>
        <th>Quantity</th>
        <th>Buy</th>
        <th>Add</th>

    </tr>

    <c:forEach var="product" items="${products}">

        <tr>

            <td>${product.id}</td>

            <td>${product.name}</td>

            <td>${product.price}</td>

            <td>${product.quantity}</td>

            <td>

                <form action="/products/buy"
                      method="post">

                    <input type="hidden"
                           name="id"
                           value="${product.id}">

                    <button type="submit">
                        Buy
                    </button>

                </form>

            </td>
            <td>
              <form action="/products/addp"
                                  method="post">

                                <input type="hidden"
                                       name="id"
                                       value="${product.id}">

                                <button type="submit">
                                    Add
                                </button>

                            </form>

                        </td>

        </tr>

    </c:forEach>

</table>

</body>

</html>