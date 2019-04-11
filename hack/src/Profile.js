import React, { Component } from 'react';
import './Profile.css';







class Profile extends Component {

    constructor(props){
        super(props);
        this.state = {
            name : props.name,
            lastName :props.lastName,
            age:props.age,
            rating:props.rating,
            description:props.description,
            pic:props.pic,
        };
    }
    render() {
        var s="";
        var t=this.state.rating
        for(let i=0;i<t;i++)
        {
            s+= '*';
        }
      return(
        
        <div>

         <div id="header1" ></div>
          <img id="avatar"  alt="t" src="https://bootdey.com/img/Content/avatar/avatar6.png"/>
          <div id="body1">
            <div id="bodyContent">

            <center>
              <p id="name"> {this.state.name}  {this.state.lastName}</p>
              <p id="info">  {this.state.age}</p>
              <p id="description">Lorem loves humus,come and eat humus with me</p>
              
              <button id="buttonContainer">
                <p>update details</p>  
              </button>              
              </center>

              </div>
              </div>
              </div>
      );
    }
  }

export default Profile;





 


