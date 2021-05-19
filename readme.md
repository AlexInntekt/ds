### Authentication endpoints

`POST http://127.0.0.1:8000/api/v1/rest-auth/login/`
{   
	"username":"test1",   
	"password":"parola123"
}   


`POST http://127.0.0.1:8000/api/v1/register`  
{   
	"username":"test1",   
	"password":"parola123",   
	"email":"test@domain.g"  
}   

`POST `
   
### Protected with token:      
`GET http://127.0.0.1:8000/api/v1/users`     
in headers add `"Authorization":"token {value of token}"`     



### Exhaustive list of endpoints   
```
admin/
api/v1/register
api/v1/rest-auth/ ^password/reset/$ [name='rest_password_reset']
api/v1/rest-auth/ ^password/reset/confirm/$ [name='rest_password_reset_confirm']
api/v1/rest-auth/ ^login/$ [name='rest_login']
api/v1/rest-auth/ ^logout/$ [name='rest_logout']
api/v1/rest-auth/ ^user/$ [name='rest_user_details']
api/v1/rest-auth/ ^password/change/$ [name='rest_password_change']
api/v1 /users [name='list_users']
```