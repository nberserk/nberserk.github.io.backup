---
layout: post
title:  "Swagger로 rest api 문서화 하기"
tags: rest swagger
---

Jetty + Jersey + swagger 조합으로 간단한 rest api 만들고, rest api 문서화하고 + 테스트 해볼 수 있는 web ui까지 구현해보는 코스.

## Jersey 로 rest api 구현하기
아래 처럼 maven 명령을 실행하면 프로젝트 구조를 만들어 준다.

```
mvn archetype:generate -DarchetypeArtifactId=jersey-quickstart-webapp -DarchetypeGroupId=org.glassfish.jersey.archetypes 
```
아래와 같은 파일들이 만들어 지고 .. 

```
rest/pom.xml
rest/src/main
rest/src/main/java/<your package>/MyResource.java
rest/src/main/webapp/index.jsp
rest/src/main/webapp/WEB-INF/web.xml
```

이 중 MyResource.java가 리소스 파일이 되는데, 리네임해서 Hello.java로 만들자. 여기에 @Path만 붙여주면 rest api 처리하는 리소스 클래스가 된다. @GET, @POST ,@PUT , @DELETE 어노테이션을 하는 것만으로 쉽게 속성을 수정할 수 있다. 더구나 @Produces 를 사용해서 POJO class를 xml 혹은 json으로 인코딩 해서 보낼 수 있다. 멋지지 않는가? (아래의 Model class는 POJO class이다. 즉, 중요하지 않다.)

```java
@Path("hello")
public class Hello {

    static Model model;
    static {
        model = new Model("Darren");
        model.setDesc("description");
    }

    @Path("/text")
    @GET
    public String getText(){
        return model.toString();
    }

    @Path("/json")
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response getJson() {
        return Response.ok().entity(model).build();
    }

    @Path("/xml")
    @GET
    @Produces(MediaType.APPLICATION_XML)
    public Response getXml(){
        return Response.ok().entity(model).build();
    }
```


## Jetty로 실행해 보기
앞단에서 rest api 구현은 해놨고 이것을 실행을 해야 하는데, tomcat등에 설치해서 하면 되지만 약간 무거운(?) 느낌이 있다. 그래서 light한 Jetty로 이 웹앱을 실행해 보자.

우선 아래 내용을 pom.xml에 추가하고

```
<plugin>
	<groupId>org.eclipse.jetty</groupId>
	<artifactId>jetty-maven-plugin</artifactId>
	<version>9.3.0.v20150612</version>
</plugin>
```

`mvn jetty:run`을 실행하면 localhost:8080으로 서버를 실행한다. 그러면 직접 rest api를 call 해 볼 수 있다. jetty:run이 무엇을 하는지 궁금하다면 [여기](http://www.eclipse.org/jetty/documentation/current/jetty-maven-plugin.html#jetty-run-goal) 를 보자. 내가 요약해주면 각 기본 디렉토리(src/main/webapp, classes in outdir)에 있는 파일들을 deploy해준다. 특정 파일에 변경이 생기면 업데이트 해주는 센스까지..

그럼 아래 url들을 차례로 브라우저에서 접근해보자. 각각 text, json, xml 포맷으로 response가 온다. 

- http://localhost:8080/rest/text
- http://localhost:8080/rest/json
- http://localhost:8080/rest/xml

## swagger integration
먼저 pom.xml 에 swagger dependency를 추가하고

```
        <dependency>
            <groupId>io.swagger</groupId>
            <artifactId>swagger-jersey2-jaxrs</artifactId>
            <version>1.5.0</version>
        </dependency>
```

web.xml. Jersey2Config는 swagger.json을 위한 것이고 기타 api.version과 basepath등을 여기서 설정해 준다.

```
    <servlet>
        <servlet-name>jersey</servlet-name>
        <servlet-class>org.glassfish.jersey.servlet.ServletContainer</servlet-class>
        <init-param>
            <param-name>jersey.config.server.provider.packages</param-name>
            <param-value>
                io.swagger.jaxrs.listing,
                com.nberserk.rest
            </param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>
    <servlet>
        <servlet-name>Jersey2Config</servlet-name>
        <servlet-class>io.swagger.jersey.config.JerseyJaxrsConfig</servlet-class>
        <init-param>
            <param-name>api.version</param-name>
            <param-value>1.0.0</param-value>
        </init-param>
        <init-param>
            <param-name>swagger.api.basepath</param-name>
            <param-value>http://localhost:8080/rest</param-value>
        </init-param>
        <load-on-startup>2</load-on-startup>
    </servlet>
```

## Swagger로 annotation추가 하기 
이제 문서화를 할 차례다. Hello class에는 `@Api, @ApiOperation` annotation으로 Model class에는 `@ApiModel, @ApiModelProperty`로 annotation을 달아주면 나중에 swagger-ui로 보면 어노테이션한 설명들이 표시가 된다.

annotation된 Hello class

```java
@Api(value="/hello", description="hello APIs")
@Path("hello")
public class Hello {

    static Model model;
    static {
        model = new Model("Darren");
        model.setDesc("description");
    }

    @ApiOperation(value = "", notes = "Gets model (text)", response = Model.class)
    @Path("/text")
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String getText(){
        return model.toString();
    }

    @ApiOperation(value = "", notes = "Gets model (json)", response = Model.class)
    @Path("/json")
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response getJson() {
        return Response.ok().entity(model).build();
    }

    @ApiOperation(value = "", notes = "Gets model (xml)", response = Model.class)
    @Path("/xml")
    @GET
    @Produces(MediaType.APPLICATION_XML)
    public Response getXml(){
        return Response.ok().entity(model).build();
    }
}
```

annotation된 Model class

```java
ApiModel(description="Model")
@XmlRootElement
public class Model {   
    String id;
    String desc;

    public Model(String id){
        this.id = id;
    }

    @ApiModelProperty(required = true, value = "id")
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

    @ApiModelProperty(value = "description")
    public String getDesc() {
        return desc;
    }

    @Override
    public String toString() {
        return "id: " + id + ", desc: " + desc;
    }
}
```

Swagger가 잘 설정되었는지를 보려면 브라우저로 [rest/swagger.json](http://localhost/rest/swagger.json) 여기 들어가서 json 파일이 보면 설정이 잘 된 것이다.

## swagger-ui

자 이제 모든 준비는 끝났다. [swagger-ui](http://petstore.swagger.io/)에 가서 `http://localhost:8080/rest/swagger.json`을 입력하면 annotation에서 기술했던 정보들이 문서화 되어서 나오고, 여기서 바로 rest api를 불러 볼 수 도 있다. 모든 개발자는 문서화를 싫어하고, 소스와 싱크를 맞추는 일 또한 노력과 정성이 들어가기 때문에 소스에 annotation만 잘 해주면 싱크도 맞춰지니까 유용한 툴이 될 것이다. 아래 스크린샷 참고.

![swagger-ui screenshot]( {{ site.url }}/assets/swagger-ui.png)









## revision history
* 2015/7/14 initial draft 

