--
-- PostgreSQL database dump
--

\restrict JsrdeQGgfasG26pVicyi7s1cJPqY3Xauu2DgSya3CocV2vqibTxzAK6V1R4DGYt

-- Dumped from database version 18.6
-- Dumped by pg_dump version 18.6

-- Started on 2026-11-04 17:03:02

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 226 (class 1259 OID 16435)
-- Name: assignment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.assignment (
    assignment_id integer NOT NULL,
    employee_id integer NOT NULL,
    position_id integer NOT NULL,
    assignment_date date NOT NULL,
    rate numeric(3,2) NOT NULL,
    CONSTRAINT assignment_rate_check CHECK (((rate > (0)::numeric) AND (rate <= (1)::numeric)))
);


ALTER TABLE public.assignment OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16434)
-- Name: assignment_assignment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.assignment ALTER COLUMN assignment_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.assignment_assignment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 220 (class 1259 OID 16390)
-- Name: department; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.department (
    department_id integer NOT NULL,
    name character varying(100) NOT NULL,
    location character varying(100) NOT NULL
);


ALTER TABLE public.department OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16389)
-- Name: department_department_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.department ALTER COLUMN department_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.department_department_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 224 (class 1259 OID 16413)
-- Name: employee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employee (
    employee_id integer NOT NULL,
    full_name character varying(150) NOT NULL,
    birth_date date NOT NULL,
    phone character varying(20) NOT NULL,
    email character varying(100) NOT NULL,
    department_id integer NOT NULL
);


ALTER TABLE public.employee OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16412)
-- Name: employee_employee_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.employee ALTER COLUMN employee_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.employee_employee_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 228 (class 1259 OID 16457)
-- Name: employee_test; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employee_test (
    test_id bigint NOT NULL,
    full_name character varying(100) NOT NULL,
    department_id integer NOT NULL,
    salary numeric(10,2) NOT NULL,
    hire_date date NOT NULL
);


ALTER TABLE public.employee_test OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 16456)
-- Name: employee_test_test_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.employee_test ALTER COLUMN test_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.employee_test_test_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 222 (class 1259 OID 16401)
-- Name: position; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."position" (
    position_id integer NOT NULL,
    name character varying(100) NOT NULL,
    salary numeric(10,2) NOT NULL,
    CONSTRAINT position_salary_check CHECK ((salary > (0)::numeric))
);


ALTER TABLE public."position" OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16400)
-- Name: position_position_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."position" ALTER COLUMN position_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.position_position_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 4893 (class 2606 OID 16445)
-- Name: assignment assignment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assignment
    ADD CONSTRAINT assignment_pkey PRIMARY KEY (assignment_id);


--
-- TOC entry 4879 (class 2606 OID 16399)
-- Name: department department_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_name_key UNIQUE (name);


--
-- TOC entry 4881 (class 2606 OID 16397)
-- Name: department department_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_pkey PRIMARY KEY (department_id);


--
-- TOC entry 4887 (class 2606 OID 16427)
-- Name: employee employee_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_email_key UNIQUE (email);


--
-- TOC entry 4889 (class 2606 OID 16425)
-- Name: employee employee_phone_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_phone_key UNIQUE (phone);


--
-- TOC entry 4891 (class 2606 OID 16423)
-- Name: employee employee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (employee_id);


--
-- TOC entry 4895 (class 2606 OID 16466)
-- Name: employee_test employee_test_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee_test
    ADD CONSTRAINT employee_test_pkey PRIMARY KEY (test_id);


--
-- TOC entry 4883 (class 2606 OID 16411)
-- Name: position position_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."position"
    ADD CONSTRAINT position_name_key UNIQUE (name);


--
-- TOC entry 4885 (class 2606 OID 16409)
-- Name: position position_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."position"
    ADD CONSTRAINT position_pkey PRIMARY KEY (position_id);


--
-- TOC entry 4896 (class 1259 OID 16467)
-- Name: idx_employee_test_salary; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_employee_test_salary ON public.employee_test USING btree (salary);


--
-- TOC entry 4898 (class 2606 OID 16446)
-- Name: assignment assignment_employee_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assignment
    ADD CONSTRAINT assignment_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employee(employee_id);


--
-- TOC entry 4899 (class 2606 OID 16451)
-- Name: assignment assignment_position_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.assignment
    ADD CONSTRAINT assignment_position_id_fkey FOREIGN KEY (position_id) REFERENCES public."position"(position_id);


--
-- TOC entry 4897 (class 2606 OID 16428)
-- Name: employee employee_department_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.department(department_id);


-- Completed on 2026-11-04 17:03:02

--
-- PostgreSQL database dump complete
--

\unrestrict JsrdeQGgfasG26pVicyi7s1cJPqY3Xauu2DgSya3CocV2vqibTxzAK6V1R4DGYt

