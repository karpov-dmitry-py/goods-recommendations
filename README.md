# Categories and products REST API management service (CRUD operations)

## Functionality:

### 1. Categories handling
 - http://127.0.0.1:8000/api/categories/ - GET, POST - multuple entities [(example)](https://www.screencast.com/t/vTUJfE7Ba6ng)
 
 - http://127.0.0.1:8000/api/categories/id/ - GET, PUT, DELETE - single entity [(example)](https://www.screencast.com/t/6LH8gorQ)
 
 - http://127.0.0.1:8000/api/categories/id/products/ - GET - all products for current category [(example)](https://www.screencast.com/t/xOgGmngX7N)
 
 - http://127.0.0.1:8000/api/categories/id/key_properties/ - GET - all key properties for current category (used for search of similar products in a category) [(example 1, ](https://www.screencast.com/t/4iCllrgl7Z) [example 2)](https://www.screencast.com/t/FJwSd2el)
 
 - http://127.0.0.1:8000/api/categories/recommendations/?price_delta=<delta:int> - GET - category info, product key properties values and **a recommended (similar) products list for each product in each category** including optional max allowed price delta variation percentage (30% by default) [(example)](https://www.screencast.com/t/G5E7DynL), 
  see also recommendations.json in code section
  
### 2. Products handling
 - http://127.0.0.1:8000/api/products/ - GET, POST - multuple entities [(example)](https://www.screencast.com/t/XCAseRHDY0N)
 
 - http://127.0.0.1:8000/api/products/id/ - GET, PUT, DELETE - single entity [(example)](https://www.screencast.com/t/sgxxtKwrbo1) 
 
 - http://127.0.0.1:8000/api/products/id/properties/ - GET - all properties for current product [(example 1, ](https://www.screencast.com/t/uEE6Ig5zR) [example 2)](https://www.screencast.com/t/mlvZDCf9j1)
  
### 3. Properties (general list) handling
 - http://127.0.0.1:8000/api/properties/ - GET, POST - multuple entities [(example)](https://www.screencast.com/t/mzBcfFChgS79)
 
 - http://127.0.0.1:8000/api/properties/id/ - GET, PUT, DELETE - single entity [(example)](https://www.screencast.com/t/5g2KDFHjj3) 
  
  - http://127.0.0.1:8000/api/properties/id/products/ - GET - all products that have current property set with a value [(example)](https://www.screencast.com/t/0Q8cAHjrsp) 

### 4. Product properties handling
 - http://127.0.0.1:8000/api/products_properties/ - GET, POST - multuple entities [(example)](https://www.screencast.com/t/jVVlGUsBJ6)
 
 - http://127.0.0.1:8000/api/products_properties/id/ - GET, PUT, DELETE - single entity [(example)](https://www.screencast.com/t/jmxZxxsjuZ) 

### 5. Category key properties handling
 - http://127.0.0.1:8000/api/categories_key_properties/ - GET, POST - multuple entities [(example)](https://www.screencast.com/t/snlBrzi624t)
 
 - http://127.0.0.1:8000/api/categories_key_properties/id/ - GET, PUT, DELETE - single entity [(example)](https://www.screencast.com/t/YnJpCZioydCJ)
