import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";

import SearchField from 'react-search-field';

import axios from "../auth/axiosConfig";

import Table from "react-bootstrap/Table";
import { createNotification } from "../reduxStore/appSlice";
import { useDispatch } from "react-redux";

// Displays All Users or specific by author
export function UsersList() {
  const [usersList, setUsersList] = useState();
  const url = '../server/api/users';
  const dispatch = useDispatch();
  function displayList(filter){     
    if (usersList && usersList.length){
      return usersList.map((user)=>{
        return(         
          <tr>
            <td>{user.id}</td>
            <td className='title'><NavLink to={'/userDetails/' + user.id} >{user.username}</NavLink></td>
            <td>{user.email}</td>
            <td>{new Date(user.date_joined).toString()}</td>
            <td>
              <span class="badge"><NavLink to={'/analysis/' + user.username} >Analysis</NavLink></span>
              <span class="badge"><NavLink to={'/recordsList/' + user.username} >Records</NavLink></span>
              <span class="badge"><NavLink to={'/requestsList/' + user.username} >Requests</NavLink></span>
            </td>
          </tr>            
        )
    })}
  }

  function search (item) {
    var users = document.getElementsByClassName("title");
    for (var i=0 ; i<users.length ;  i++){
      if (!users[i].textContent.toUpperCase().match(item.toUpperCase())){
        users[i].parentElement.style.display = "none"
      }
      else
        users[i].parentElement.style.display = ""  
    }
  }
  
  useEffect(() => {  
    axios
    .get(url)
    .then(res => {
      setUsersList(res.data);
    })
    .catch( (error) => dispatch(createNotification([error.message, 'error'])))  
  }, [])
  
  return (
    <div class='bookList'>
      <h1>Users List</h1>
      <SearchField 
        placeholder='Search By Username'
        onChange={search}
      />
      <hr/>
        <Table striped bordered hover>
          <thead>
            <tr>
              <th>ID</th>
              <th>Username</th>
              <th>Email</th>
              <th>Joining Date</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {displayList()}
          </tbody>
        </Table>
    </div>
  )
}
  