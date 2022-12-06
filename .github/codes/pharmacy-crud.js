import './App.css';
import React from 'react';
import SideNav from "./SideNav.js";
import TopNav from "./TopNav.js";
import searchIcon from "./images/search.png"
import penIcon from "./images/pen.png"
import trashCanIcon from "./images/trash-can.png"

function App() {
  return (
    <div className='container'>
      <div className='content'>
      <SideNav/>
      <TopNav/>
        <div className='search-box'>
          <div className='search-icon'>
            <img src={searchIcon} alt="search" className='search-icon'/>
          </div>
          <input className='search-bar' type="text" placeholder='Search...'></input>
        </div>

        <div className='add-button-box'>
          <p className='add-new'>Add new pharmacy</p>
        </div>

        <div className='pharmacy-list-box'>
          <ul className='pharmacy-list'>
            <li className='pharmacy-element'>
              <p className='title label'>Giray Pharmacy</p>
              <p className='date label'>Last modified: 3.12.2022</p>
              <p className='address label'>Reşitpaşa Mahallesi Spor Yolu Sokak No:11</p>
              <div className='icon-box'>
                <div className='icon'>
                  <img src={penIcon} alt="edit" className="icon"/>
                </div>
                <div className='icon'>
                  <img src={trashCanIcon} alt="delete" className="icon"/>
                </div>
              </div>
            </li>
            <li className='pharmacy-element'>
              <p className='title label'>Giray Pharmacy</p>
              <p className='date label'>Last modified: 3.12.2022</p>
              <p className='address label'>Reşitpaşa Mahallesi Spor Yolu Sokak No:11</p>
              <div className='icon-box'>
                <div className='icon'>
                  <img src={penIcon} alt="edit" className="icon"/>
                </div>
                <div className='icon'>
                  <img src={trashCanIcon} alt="delete" className="icon"/>
                </div>
              </div>
            </li>
            <li className='pharmacy-element'>
              <p className='title label'>Giray Pharmacy</p>
              <p className='date label'>Last modified: 3.12.2022</p>
              <p className='address label'>Reşitpaşa Mahallesi Spor Yolu Sokak No:11</p>
              <div className='icon-box'>
                <div className='icon'>
                  <img src={penIcon} alt="edit" className="icon"/>
                </div>
                <div className='icon'>
                  <img src={trashCanIcon} alt="delete" className="icon"/>
                </div>
              </div>
            </li>
            <li className='pharmacy-element'>
              <p className='title label'>Giray Pharmacy</p>
              <p className='date label'>Last modified: 3.12.2022</p>
              <p className='address label'>Reşitpaşa Mahallesi Spor Yolu Sokak No:11</p>
              <div className='icon-box'>
                <div className='icon'>
                  <img src={penIcon} alt="edit" className="icon"/>
                </div>
                <div className='icon'>
                  <img src={trashCanIcon} alt="delete" className="icon"/>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>

    </div>
  );
}

export default App;
