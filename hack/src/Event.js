import React, { Component } from 'react';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import Drawer from 'react-drag-drawer'

//import "./Event.css";

class Event extends Component {
  constructor(props){
    super(props);
    this.state = {
        name : props.name,
        description : props.description,
        evPic : props.evPic,
        howFar : props.howFar, 
        attending : props.attending,
        required :  props.required
        
    };
}
    render() {
      
      return (
        <div>
          <Card style={{ width: '40rem' ,height: '50rem'}}>
            <Card.Img variant="top" src="http://www.jbryant.eu/recipes/Humous.jpg" />
            <Card.Body>
              <Card.Title>{this.props.name}</Card.Title>
              <Card.Text>
                Some quick example text to build on the card title and make up the bulk of
                the card's content.
              </Card.Text>
              <Button variant="primary">Go somewhere</Button>
            </Card.Body>
          </Card>;
          <Drawer
          open={true}
          onRequestClose={this.toggle}
          modalElementClass={myCustomDrawerClassName}
>
            <div>Hey Im inside a drawer!</div>
          </Drawer>
        </div>
        
      );
    }
  }

export default Event;