<img src = "http://r3.masstransitmag.com/files/base/image/MASS/2014/04/16x9/320x180/greystone-logo_11392262.jpg" align = "right" height="142" width="342">

# greyco_api
A Simple Django Rest Application

Requirements
=======

* Python 2.7.x 

And the following modules (found in [requirements.txt](https://github.com/vinothkumar6692/greyco_api/greystone/requirements.txt)):

  Django==1.8.4
  django-autoslug==1.7.2
  django-filter==0.14.0
  djangorestframework==3.4.6

Setup
=======

Follow the steps below to setup the server on your local machine.

* Clone the repository using 

```bash
$ git clone git@github.com:vinothkumar6692/greyco_api.git
```

* Change into the directory /greycode using the command below

```bash
$ cd greystone
```

* Install all the requirements specified in the [requirements.txt](https://github.com/vinothkumar6692/greyco_api/greystone/requirements.txt)):

```bash
$ python setup.py install
```

* Start the server using 

```bash
$ python manage.py runserver
```

API Documentation
=======


---
### GET Messages
---

Return a JSON list of Message objects that are currently being stored.

* **URL**

  `/messages/`

* **Method:**
  
  `GET`
  
*  **URL Params**

   **Required:**
 
     `*None*`

   **Optional:**
 
     `*None*`

* **Success Response:**

  * **Code:** 200 <br />


--
### POST Message
---

Should accept a “message_text” parameter that creates a Message object and stores the value.

* **URL**

`/messages/`

* **Method:**

`POST`

*  **URL Params**

**Required:**

  `*None*`

**Optional:**

  `*None*`

* **Data Params**

**Required:**

JSON Data Object

{ “message_text”: “hello world” }

None

* **Success Response:**

* **Code:** 200 <br />

* **Content:**
  
  ```json
  {“message”: {“message_text”: “hello world”, “id”: 1}]}}
  ``` 

---
### DELETE Message
---

Delete the message with the given id

* **URL**

`/messages/:id`

* **Method:**

`DELETE`

*  **URL Params**

**Required:**

 `*id*`
 
**Optional:**

  `*None*`

* **Data Params**

**Required:**

  `*None*`

**Optional:**

  `*None*`

* **Success Response:**

* **Code:** 200 <br />
