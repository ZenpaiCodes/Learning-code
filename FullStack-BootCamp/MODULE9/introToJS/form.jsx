import React from "react";

const Form = () => {
  const formData = [
    { field: "name", type: "text", label: "Full Name", error: "true" },
    { field: "email", type: "email", label: "Email", error: "true" },
    { field: "password", type: "password", label: "Password", error: "true" },
    { field: "confirmPassword", type: "password", label: "Confirm Password", error: "true" },
  ];
  
  const createFromFields = () => formData.map(item => (
    <div className="wrapper">
      <div className="field">
        <label htmlFor={item.field}>{item.label}</label>
        <input type={item.type} name={item.field} id={item.field} placeholder="Type your full name..." />
      </div>
      {item.error && <small>{`Full name is required ${item.field}`}</small>}
    </div>
  ))

  return (
    <form className="container">
      {createFromFields()}
      <input type="submit" value="submit"/>
    </form>
  )
};