// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract BridgeStacks {
    address public owner;
    IERC20 public token;

    constructor(address _token) {
        owner = msg.sender;
        token = IERC20(_token);
    }

    function unlockTokens(address recipient, uint256 amount) external {
        require(msg.sender == owner, "You are not the owner of this token!");
        token.transfer(recipient, amount);
    }
}