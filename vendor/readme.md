# Project Title

vendor management system

## Description

Develop a Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics.
## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* git clone https://github.com/Rohit2998/vendor-management.git
pip install -r requirements.txt

### Executing program


```
cd vendor
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
command to run if program contains helper info
```
```
### Import postman_collection in postman
```
for smooth use
json file used : postman_collection.json 
```
```


## APIs Endpoint
    please refer postman collection 
    ● POST /api/vendors/: Create a new vendor.
    ● GET /api/vendors/: List all vendors.
    ● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
    ● PUT /api/vendors/{vendor_id}/: Update a vendor's details.
    ● DELETE /api/vendors/{vendor_id}/: Delete a vendor.
    ● POST /api/purchase_orders/: Create a purchase order.
    ● GET /api/purchase_orders/: List all purchase orders with an option to filter by
    vendor.
    ● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
    ● PUT /api/purchase_orders/{po_id}/: Update a purchase order.
    ● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.