// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract BridgeEth {
    address public owner;
    IERC20 public token;

    constructor(address _token) {
        owner = msg.sender;
        token = IERC20(_token);
    }

    function lockTokens(uint256 amount) external {
        token.transferFrom(msg.sender, address(this), amount);
    }
}