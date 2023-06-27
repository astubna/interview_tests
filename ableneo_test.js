import React from "react";
import { render } from "react-dom";
import App from "./App";

// You have users object reference from previous exercise.
// Write functions what will get various data from users object.
const users = [
  { id: 1, name: "c", role: "admin", score: 2 },
  { id: 2, name: "b", role: "user", score: 10 },
  { id: 3, name: "a", role: "user", score: 30 }
];

// 0.Write stateles component which will print all user names in list
function UsersComponent({ users }) {
  return (
    <ul>
      {users.map((item) => {
        return (
          <li>
            {Object.keys(users[0])[1]}: {item.name}
          </li>
        );
      })}
    </ul>
  );
}
/* output 
<ul>
  <li>name: c</li>
  <li>name: b</li>
  <li>name: a</li>
</ul>
*/

// 1.Write function that will return user by id.
function getById(users, id = 2) {
  return users.find((users) => users.id === id);
} // output {id: 2, name: "b", role: "user", score: 10}

// 2.Write function that will return users by role.
function getByRole(users, role = "admin") {
  const user_by_role = users.find((users) => users.role === role);
  return Array(user_by_role);
} // output [{id: 1, name: "c", role: "admin", score: 2}]

// 3.Write function that will return object with roles as keys and values as number of role occurrences.
function getRoleMetrics(users) {
  let adminCount = 0;
  let userCount = 0;
  for (let i = 0; i < users.length; i++) {
    if (users[i].role === "admin") {
      adminCount += 1;
    }
    if (users[i].role === "user") {
      userCount += 1;
    }
  }
  const rolesCountObject = {
    admin: adminCount,
    user: userCount
  };
  return rolesCountObject;
}

// output {admin: 1, user: 2}

// 4.Write function that will return users ordered by name.
function getOrderedByName(users) {
  const copiedUsers = users.slice();
  copiedUsers.sort(function (a, b) {
    if (a.name < b.name) {
      return -1;
    }
    if (a.name > b.name) {
      return 1;
    }
    return 0;
  });
  return copiedUsers;
} // output order [{id:3, name: "a",...},{id:2, name: "b",...},{id:1, name: "c", ...}]

// 5.Write function that will return users ordered by highest score.
function getOrderedByScore(users) {
  const copiedUsers = users.slice();
  copiedUsers.sort(function (a, b) {
    if (a.score > b.score) {
      return -1;
    }
    if (a.score < b.score) {
      return 1;
    }
    return 0;
  });
  return copiedUsers;
} // output order [{id:3, score: 30, ...},{id:2, score: 10, ...}, {id:1, score: 2,...}]

// 6. Write function that will return new users collection with added user.
function addUser(users,
  userToAdd = { id: 4, name: "d", role: "user", score: 50 }) {
  
  const myUpdatedUsers = [...users, userToAdd]
  return myUpdatedUsers; 
/*  users,
  userToAdd = { id: 4, name: "d", role: "user", score: 50 }
) {
  let copiedUsers = users.slice();
  copiedUsers.push(userToAdd);
  return copiedUsers; */
} // output length === 4

// 7. Write function that will return new users collection without removed user.
function removeUserById(users, userId = 2) {
  return users.filter((users) => users.id !== userId);
} // output length === 2

render(
  <App
    users={users}
    UsersComponent={UsersComponent}
    getById={getById}
    getByRole={getByRole}
    getRoleMetrics={getRoleMetrics}
    getOrderedByName={getOrderedByName}
    getOrderedByScore={getOrderedByScore}
    addUser={addUser}
    removeUserById={removeUserById}
  />,
  document.getElementById("root")
);
