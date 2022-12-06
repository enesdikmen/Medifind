import React from 'react';
import './SideNav.css'

const SideNav = (props) => {
    return (
        <nav class="nav">
        <ul class="nav-list">
            <li className='nav-item'>
                <div className='medifind-box'>
                    <p className='medifind'>M</p>
                    <span class="medifind-rest">EDIFIND</span>
                </div>
                
            </li>
          <li class="nav-item">
            <a href="home.html" class="nav-link">
              <svg
                aria-hidden="true"
                focusable="false"
                data-prefix="fad"
                data-icon="house"
                role="img"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 600 500"
                class="svg-inline--fa fa-house fa-w-12 fa-5x"
              >
                <g class="fa-group">
                  <path
                    fill="currentColor"
                    d="M575.8 255.5c0 18-15 32.1-32 32.1h-32l.7 160.2c0 2.7-.2 5.4-.5 8.1V472c0 22.1-17.9 40-40 40H456c-1.1 0-2.2 0-3.3-.1c-1.4 .1-2.8 .1-4.2 .1H416 392c-22.1 0-40-17.9-40-40V448 384c0-17.7-14.3-32-32-32H256c-17.7 0-32 14.3-32 32v64 24c0 22.1-17.9 40-40 40H160 128.1c-1.5 0-3-.1-4.5-.2c-1.2 .1-2.4 .2-3.6 .2H104c-22.1 0-40-17.9-40-40V360c0-.9 0-1.9 .1-2.8V287.6H32c-18 0-32-14-32-32.1c0-9 3-17 10-24L266.4 8c7-7 15-8 22-8s15 2 21 7L564.8 231.5c8 7 12 15 11 24z"
                  />
                </g>
              </svg>
              <span class="link-text">Home</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="pharmacy.html" class="nav-link">
              <svg
                aria-hidden="true"
                focusable="false"
                data-prefix="fad"
                data-icon="house"
                role="img"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 600 500"
                class="svg-inline--fa fa-house fa-w-12 fa-5x"
              >
                <g class="fa-group">
                  <path
                    fill="currentColor"
                    d="M222.6 43.2l-.2 4.8H288c53 0 96 43 96 96s-43 96-96 96H248V160h40c8.8 0 16-7.2 16-16s-7.2-16-16-16H248 220l-4.5 144H256c53 0 96 43 96 96s-43 96-96 96H240V384h16c8.8 0 16-7.2 16-16s-7.2-16-16-16H213l-3.1 99.5L208.5 495l0 1c-.3 8.9-7.6 16-16.5 16s-16.2-7.1-16.5-16l0-1-1-31H136c-22.1 0-40-17.9-40-40s17.9-40 40-40h36l-1-32H152c-53 0-96-43-96-96c0-47.6 34.6-87.1 80-94.7V256c0 8.8 7.2 16 16 16h16.5L164 128H136 122.6c-9 18.9-28.3 32-50.6 32H56c-30.9 0-56-25.1-56-56S25.1 48 56 48h8 8 89.5l-.1-4.8L161 32c0-.7 0-1.3 0-1.9c.5-16.6 14.1-30 31-30s30.5 13.4 31 30c0 .6 0 1.3 0 1.9l-.4 11.2zM64 112c8.8 0 16-7.2 16-16s-7.2-16-16-16s-16 7.2-16 16s7.2 16 16 16z"
                  />
                </g>
              </svg>
              <span class="link-text">Pharmacy</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link">
              <svg
                aria-hidden="true"
                focusable="false"
                data-prefix="fad"
                data-icon="house"
                role="img"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 600 500"
                class="svg-inline--fa fa-house fa-w-12 fa-5x"
              >
                <g class="fa-group">
                  <path
                    fill="currentColor"
                    d="M64 144c0-26.5 21.5-48 48-48s48 21.5 48 48V256H64V144zM0 144V368c0 61.9 50.1 112 112 112s112-50.1 112-112V189.6c1.8 19.1 8.2 38 19.8 54.8L372.3 431.7c35.5 51.7 105.3 64.3 156 28.1s63-107.5 27.5-159.2L427.3 113.3C391.8 61.5 321.9 49 271.3 85.2c-28 20-44.3 50.8-47.3 83V144c0-61.9-50.1-112-112-112S0 82.1 0 144zm296.6 64.2c-16-23.3-10-55.3 11.9-71c21.2-15.1 50.5-10.3 66 12.2l67 97.6L361.6 303l-65-94.8zM491 407.7c-.8 .6-1.6 1.1-2.4 1.6l4-2.8c-.5 .4-1 .8-1.6 1.2z"
                  />
                </g>
              </svg>
              <span class="link-text">Medicine</span>
            </a>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link">
              <svg
                aria-hidden="true"
                focusable="false"
                data-prefix="fad"
                data-icon="house"
                role="img"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 600 500"
                class="svg-inline--fa fa-house fa-w-12 fa-5x"
              >
                <g class="fa-group">
                  <path
                    fill="currentColor"
                    d="M336 352c97.2 0 176-78.8 176-176S433.2 0 336 0S160 78.8 160 176c0 18.7 2.9 36.8 8.3 53.7L7 391c-4.5 4.5-7 10.6-7 17v80c0 13.3 10.7 24 24 24h80c13.3 0 24-10.7 24-24V448h40c13.3 0 24-10.7 24-24V384h40c6.4 0 12.5-2.5 17-7l33.3-33.3c16.9 5.4 35 8.3 53.7 8.3zm40-176c-22.1 0-40-17.9-40-40s17.9-40 40-40s40 17.9 40 40s-17.9 40-40 40z"
                  />
                </g>
              </svg>
              <span class="link-text">Password Change</span>
            </a>
          </li>
        </ul>
      </nav>
    );
};
export default SideNav;