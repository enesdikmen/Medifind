import './App.css';
import React from 'react';
import SideNav from "./SideNav.js";
import TopNav from "./TopNav.js";
import searchIcon from "./images/search.png"
import penIcon from "./images/pen.png"
import trashCanIcon from "./images/trash-can.png"
import arrowIcon from "./images/right-arrow.png"

function App() {
  return (
    <div className='container'>
      <SideNav/>
      <TopNav/>
      <div className='content'>
        <div className='search-box'>
          <div className='search-icon'>
            <img src={searchIcon} alt="search" className='search-icon'/>
          </div>
          <input className='search-bar' type="text" placeholder='Search...'></input>
        </div>

        <p className='add-new'>Add new medicine</p>

        <div className='medicine-list-box'>
          <ul className='medicine-list'>
            <li className='medicine-element label'>
              <p className='title label'>Parol</p>
              <img src={arrowIcon} alt="arrow" className='arrow-icon icon' />
              <div className='info-box'>
                <p className='id info'>ID: 12345</p>
                <p className='quantity info'>#: 257</p>
              </div>
              <div className='icon-box'>
                <img className='icon2' src={penIcon} alt="pen"/>
                <img className='icon2' src={trashCanIcon} alt="trash"/>
              </div>
            </li>
            <li className='medicine-element label'>
              <p className='title label'>Parol</p>
              <img src={arrowIcon} alt="arrow" className='arrow-icon icon' />
              <div className='info-box'>
                <p className='id info'>ID: 12345</p>
                <p className='quantity info'>#: 257</p>
              </div>
              <div className='icon-box'>
                <img className='icon2' src={penIcon} alt="pen"/>
                <img className='icon2' src={trashCanIcon} alt="trash"/>
              </div>
            </li>
            <li className='medicine-element label'>
              <p className='title label'>Parol</p>
              <img src={arrowIcon} alt="arrow" className='arrow-icon icon' />
              <div className='info-box'>
                <p className='id info'>ID: 12345</p>
                <p className='quantity info'>#: 257</p>
              </div>
              <div className='icon-box'>
                <img className='icon2' src={penIcon} alt="pen"/>
                <img className='icon2' src={trashCanIcon} alt="trash"/>
              </div>
            </li>
            <li className='medicine-element label'>
              <p className='title label'>Parol</p>
              <img src={arrowIcon} alt="arrow" className='arrow-icon icon' />
              <div className='info-box'>
                <p className='id info'>ID: 12345</p>
                <p className='quantity info'>#: 257</p>
              </div>
              <div className='icon-box'>
                <img className='icon2' src={penIcon} alt="pen"/>
                <img className='icon2' src={trashCanIcon} alt="trash"/>
              </div>
            </li>
            <li className='medicine-element label'>
              <p className='title label'>Parol</p>
              <img src={arrowIcon} alt="arrow" className='arrow-icon icon' />
              <div className='info-box'>
                <p className='id info'>ID: 12345</p>
                <p className='quantity info'>#: 257</p>
              </div>
              <div className='icon-box'>
                <img className='icon2' src={penIcon} alt="pen"/>
                <img className='icon2' src={trashCanIcon} alt="trash"/>
              </div>
            </li>
            <li className='medicine-element label'>
              <p className='title label'>Parol</p>
              <img src={arrowIcon} alt="arrow" className='arrow-icon icon' />
              <div className='info-box'>
                <p className='id info'>ID: 12345</p>
                <p className='quantity info'>#: 257</p>
              </div>
              <div className='icon-box'>
                <img className='icon2' src={penIcon} alt="pen"/>
                <img className='icon2' src={trashCanIcon} alt="trash"/>
              </div>
            </li>
            <li className='medicine-element label'>
              <p className='title label'>Parol</p>
              <img src={arrowIcon} alt="arrow" className='arrow-icon icon' />
              <div className='info-box'>
                <p className='id info'>ID: 12345</p>
                <p className='quantity info'>#: 257</p>
              </div>
              <div className='icon-box'>
                <img className='icon2' src={penIcon} alt="pen"/>
                <img className='icon2' src={trashCanIcon} alt="trash"/>
              </div>
            </li>
            <li className='medicine-element label'>
              <p className='title label'>Parol</p>
              <img src={arrowIcon} alt="arrow" className='arrow-icon icon' />
              <div className='info-box'>
                <p className='id info'>ID: 12345</p>
                <p className='quantity info'>#: 257</p>
              </div>
              <div className='icon-box'>
                <img className='icon2' src={penIcon} alt="pen"/>
                <img className='icon2' src={trashCanIcon} alt="trash"/>
              </div>
            </li>
            <li className='medicine-element label'>
              <p className='title label'>Parol</p>
              <img src={arrowIcon} alt="arrow" className='arrow-icon icon' />
              <div className='info-box'>
                <p className='id info'>ID: 12345</p>
                <p className='quantity info'>#: 257</p>
              </div>
              <div className='icon-box'>
                <img className='icon2' src={penIcon} alt="pen"/>
                <img className='icon2' src={trashCanIcon} alt="trash"/>
              </div>
            </li>
            <li className='medicine-element label'>
              <p className='title label'>Parol</p>
              <img src={arrowIcon} alt="arrow" className='arrow-icon icon' />
              <div className='info-box'>
                <p className='id info'>ID: 12345</p>
                <p className='quantity info'>#: 257</p>
              </div>
              <div className='icon-box'>
                <img className='icon2' src={penIcon} alt="pen"/>
                <img className='icon2' src={trashCanIcon} alt="trash"/>
              </div>
            </li>
          </ul>
        </div>

      </div>

    </div>
  );
}

export default App;
