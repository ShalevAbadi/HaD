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
        <div id="profile">
            <img  id="profilePicture" alt="profile" src ={this.state.pic} />
            <p>
                name = {this.state.name}  {this.state.lastName}
            </p>
            <p>
                age = {this.state.age}
            </p>
            <p>
            {s}
            </p>
            <button>update details</button>
        </div>
      );
    }
  }

export default Profile;