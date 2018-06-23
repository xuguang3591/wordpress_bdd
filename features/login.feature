Feature: Login 

  @login
  Scenario: Success
    Given go to login page
    When login with guang safe3600
    Then redirect to dashboard page
    And display hello guang

  @failed
  Scenario Outline: Failed
    Given go to login page
    When let us login with incorrect <username> and incorrect <password> 
    Then should display error <message>

	Examples: data
	| username         | password         | message  								|
	| guang 		   | incorrect        | 错误：为用户名guang指定的密码不正确。 忘记密码？  |
	| empty 		   | safe3600         | 错误：用户名一栏为空。  				|
	| guang 		   | empty        	  | 错误：密码一栏为空。  				    |

  @create_post
  Scenario: Success Create Post
    Given go to login page
    When login with guang safe3600
    When create a post with title and content
    Then the new created post should be existed 

  @delete_post
  Scenario: Success Delete Post
    Given go to login page
    When login with guang safe3600
    When create a post with title and content
    When delete the new created post
    Then the new created post should not exist

