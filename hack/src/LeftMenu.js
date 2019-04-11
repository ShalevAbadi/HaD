import React, { Component } from 'react';
import './leftMenu.css';
import ReactDOM from 'react-dom';
import App from './App';
import Profile from './Profile';
import EventsList from './EventsList';


import SideNav, { Toggle, Nav, NavItem, NavIcon, NavText } from '@trendmicro/react-sidenav';

// Be sure to include styles at some point, probably during your bootstraping
import '@trendmicro/react-sidenav/dist/react-sidenav.css';

class LeftMenu extends Component {

    constructor(props){
        super(props);
        this.state = {
            
        };
        this.goToPage = this.goToPage.bind(this);
    }
    goToPage(pageID){
        var returnValue;
        {
          var imgSrc = "data:image/jpeg;base64,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"; 
      }
        switch(pageID)
        {
            case 0:
            returnValue = <Profile pic ={imgSrc}  rating={5} name="aviv" lastName="mahulya" age={25}/>;
            break;
            case 1:
            returnValue = <EventsList/>;
            break;
            default:
        }
        ReactDOM.render(returnValue, document.getElementById('mainFrame'));
    }
    render() {
      var co = this;
      /*
      return(
          <div>
        <button id="myProfile" onClick = {()=>{
          co.goToPage(0);
        }}>my profile</button>
      <button id="events" onClick = {()=>{
          co.goToPage(1);
        }}>show events</button>
      </div>
      );
      */
     return(
      <div>
        <SideNav
    onSelect={(selected) => {
        if(selected == 'profile')
        {
          co.goToPage(0);
        }
        else if(selected == 'Events')
        {
            co.goToPage(1);
        }
    }}
>
    <SideNav.Toggle />
    <SideNav.Nav defaultSelected="home">
        <NavItem eventKey="profile">
            <NavIcon>
                <i className="fa fa-fw fa-home" style={{ fontSize: '1.75em' }} />
            </NavIcon>
            <NavText>
                profile
            </NavText>
        </NavItem>
        <NavItem eventKey="Events">
            <NavIcon>
                <i className="fa fa-fw fa-line-chart" style={{ fontSize: '1.75em' }} />
            </NavIcon>
            <NavText>
                Charts
            </NavText>
            
        </NavItem>
    </SideNav.Nav>
</SideNav>
      </div>
     );
    }
  }

export default LeftMenu;